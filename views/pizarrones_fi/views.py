from flask import Flask, render_template, redirect, url_for, request, abort,\
    session, make_response, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os
    # FORMULARIO
from forms.forms import *
from forms.forms_fi import *

app = Flask(__name__)

pizarron_fi = Blueprint('pizarron_fi', __name__, template_folder='templates', static_folder='static', static_url_path='/static/upload')

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu')
@login_required
def menu_pilares_fi():
    return render_template("pilares/FI/menu_pilares_fi.html")

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero')
@login_required
def pizarron():
    from models.models import Notificaciones
    noti = Notificaciones.query.all()
        # Numero de noti
    lista = ((c.numero)for c in Notificaciones.query.all())
    suma = [lista for lista in lista]
    largo = len(suma)
    from models.models_mission_vision import Mission_fi, db
    from models.models_cbn import Cbn_fi, db
    from models.models_pilarlossmap import Pilarlossmap_fi, db
    from models.models_pilar_swot import Pilar_swot_fi, db
    id = '1'
    photo_1 = Mission_fi.query.filter_by(id=id)
    id = '2'
    photo_2 = Mission_fi.query.filter_by(id=id)
    id = '3'
    photo_3 = Mission_fi.query.filter_by(id=id)
    id = '4'
    photo_4 = Mission_fi.query.filter_by(id=id)
    dato = Cbn_fi.query.all()
    pilar = Pilarlossmap_fi.query.all()
    pilar_swot = Pilar_swot_fi.query.all()
    return render_template("tablero_fi_proto.html", dato=dato, pilar=pilar, photo_1=photo_1, photo_2=photo_2, photo_3=photo_3, 
                            photo_4=photo_4, pilar_swot=pilar_swot, noti=noti, largo=largo)

#@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero')
#@login_required
#def pizarron():
#    return render_template("tablero_fi.html")
###============================================ MISSION AND VISION ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/mision', methods=["get", "post"])
@login_required
def tablero_fi_mision():
    from models.models_mission_vision import Mission_fi, db
    from models.models import Auditor_comentario, db
    id = '1'
    articulos = Mission_fi.query.filter_by(id=id)
        # COMENTARIO
    comentario = Auditor_comentario.query.all()[:1]
        # COMENTARIO EDIT
    id = '1'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_mision"))
    return render_template("Mission_vision/mission.html", articulos=articulos, form=form, comentario=comentario)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/mision/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_mision_fi_edit(id):
    from models.models_mission_vision import Mission_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    art = Mission_fi.query.get(id)
    if art is None:
        abort(404)
    form = FormMission_fi(obj=art)
    if form.validate_on_submit():
        # Borramos la imagen anterior si hemos subido una nueva
        if form.photo.data:
            os.remove(app.root_path+'/static/upload/'+art.image)
            try:
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + '/static/upload/' + nombre_fichero)
            except:
                nombre_fichero = ''
        else:
            nombre_fichero = art.image
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_mision"))
    return render_template("Mission_vision/mission_edit.html", form=form)

###============================================ ORGANIGRAMA ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/organigrama', methods=["get", "post"])
@login_required
def tablero_fi_organigrama():
    from models.models_organigrama import Organigrama_fi
    from models.models import Auditor_comentario, db
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[5:6]
    # COMENTARIO EDIT
    id = '6'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_organigrama"))
        # MIEMBROS
    todo = Organigrama_fi.query.all()[1:]
    lider = Organigrama_fi.query.all()[0:1]
    return render_template("Organigrama/organigrama-pilar.html", form=form, comentario=comentario, todo=todo, lider=lider)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/organigrama/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_organigrama_edit(id):
    from models.models_organigrama import Organigrama_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    art = Organigrama_fi.query.get(id)
    if art is None:
        abort(404)
    form = FormOrganigrama_fi(obj=art)
    if form.validate_on_submit():
        # Borramos la imagen anterior si hemos subido una nueva
        if form.photo.data:
            os.remove(app.root_path+'/static/upload/organigrama/'+art.image)
            try:
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + '/static/upload/organigrama/' + nombre_fichero)
            except:
                nombre_fichero = ''
        else:
            nombre_fichero = art.image
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_organigrama"))
    return render_template("Organigrama/organigrama-pilar_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/organigrama/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_organigrama_delete(id):
    from models.models_organigrama import Organigrama_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    art = Organigrama_fi.query.get(id)
    if art is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            if art.image != '':
                os.remove(app.root_path+'/static/upload/organigrama/'+art.image)
            db.session.delete(art)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_organigrama"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, art=art)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/organigrama/new', methods=["get", "post"])
@login_required
def tablero_fi_organigrama_new():
    from models.models_organigrama import Organigrama_fi, db
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormOrganigrama_fi()
    if form.validate_on_submit():
        try:
            f = form.photo.data
            nombre_fichero = secure_filename(f.filename)
            f.save(app.root_path + '/static/upload/organigrama/' + nombre_fichero)
        except:
            nombre_fichero = ''
        art = Organigrama_fi()
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_organigrama"))
    else:
        return render_template("Organigrama/organigrama-pilar_edit.html", form=form)

###============================================ GRAFICA TEAM CAPABILITY ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/grafica-capability', methods=["get", "post"])
@login_required
def tablero_fi_graficacapability():
    from models.models import Auditor_comentario, db
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[11:12]
    # COMENTARIO EDIT
    id = '12'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_graficacapability"))
    return render_template("Graph_team_capability/grafica-capability.html", form=form, comentario=comentario)

###============================================ PILLAR SWOT ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-swot', methods=["get", "post"])
@login_required
def tablero_fi_pilarswot():
    from models.models_mission_vision import Mission_fi, db
    from models.models import Auditor_comentario, db
    from models.models_pilar_swot import Pilar_swot_fi, db
    dato = Pilar_swot_fi.query.all()
    id = '3'
    articulos = Mission_fi.query.filter_by(id=id)
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[2:3]
    # COMENTARIO EDIT
    id = '3'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarswot"))
    return render_template("Pillar_swot/pilar-swot.html", dato=dato, articulos=articulos, form=form, comentario=comentario)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-swot/new', methods=["get", "post"])
@login_required
def tablero_fi_pilarswot_new():
    from models.models_pilar_swot import Pilar_swot_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormPilar_swot_fi(request.form)
    if form.validate_on_submit():
        cat = Pilar_swot_fi(workprocess=form.workprocess.data, dueño=form.dueño.data, back_up=form.back_up.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarswot"))
    else:
        return render_template("Pillar_swot/pilar-swot_edit_tabla.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-swot/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_pilarswot_edit(id):
    from models.models_mission_vision import Mission_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    art = Mission_fi.query.get(id)
    if art is None:
        abort(404)
    form = FormMission_fi(obj=art)
    if form.validate_on_submit():
        # Borramos la imagen anterior si hemos subido una nueva
        if form.photo.data:
            os.remove(app.root_path+'/static/upload/'+art.image)
            try:
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + '/static/upload/' + nombre_fichero)
            except:
                nombre_fichero = ''
        else:
            nombre_fichero = art.image
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarswot"))
    return render_template("Pillar_swot/pilar-swot_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-swot/<id>/edit/workprocess', methods=["get", "post"])
@login_required
def tablero_fi_pilarswot_edit_tabla(id):
    from models.models_pilar_swot import Pilar_swot_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Pilar_swot_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormPilar_swot_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarswot"))
    return render_template("Pillar_swot/pilar-swot_edit_tabla.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-swot/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_pilarswot_delete(id):
    from models.models_pilar_swot import Pilar_swot_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Pilar_swot_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarswot"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)
###============================================ PLAN 90 DIAS ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/plan-90-dias', methods=["get", "post"])
@login_required
def tablero_fi_plandias():
    from models.models import Auditor_comentario, db
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[8:9]
    # COMENTARIO EDIT
    id = '9'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_plandias"))
    return render_template("Plan_90_dias/90-dias.html", form=form, comentario=comentario)

###============================================ SYSTEM AND TOOLS GRAPH ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/grafica-sistemas-herramienta', methods=["get", "post"])
@login_required
def tablero_fi_graficasistemaherramienta():
    from models.models import Auditor_comentario, db
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[12:13]
    # COMENTARIO EDIT
    id = '13'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_graficasistemaherramienta"))
    return render_template("Graph_system_tools/grafica-sistemas-herramienta.html", form=form, comentario=comentario)

###============================================ ESTATUS PERDIDAS ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/status-loss', methods=["get", "post"])
@login_required
def tablero_fi_statusperdidas():
    from models.models import Auditor_comentario, db
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[13:14]
    # COMENTARIO EDIT
    id = '14'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_statusperdidas"))
    return render_template("Estatus_perdidas/estatus-perdidas.html", form=form, comentario=comentario)

###============================================ TEAM CAPABILITY ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-capability', methods=["get", "post"])
@login_required
def tablero_fi_tcapability():
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_fi, Team_capability_fi, db
    from models.models import Auditor_comentario, db
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[9:10]
    # COMENTARIO EDIT
    id = '10'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcapability"))
    # OPERACIONES
        # Acreditacion
    lista = ((c.acreditacion)for c in Teamcapability_fi.query.all())
    suma = [lista for lista in lista]
    largo = len(suma)
    suma_lista = sum(suma)
    promedio_acreditacion = suma_lista / largo
        # Calificacion
    lista_cal = ((c.calificacion)for c in Teamcapability_fi.query.all())
    suma_cal = [lista for lista in lista_cal]
    largo_cal = len(suma_cal)
    suma_lista_cal = sum(suma_cal)
    promedio_calificacion = suma_lista_cal / largo_cal
    # PORCENTAJE BASIC CONCEPT
    basic_1 = [(c.basic_1_leader)for c in Team_capability_fi.query.all()]
    basic_2 = [(c.basic_2_leader)for c in Team_capability_fi.query.all()]
    basic_3 = [(c.basic_3_leader)for c in Team_capability_fi.query.all()]
    basic_4 = [(c.basic_4_leader)for c in Team_capability_fi.query.all()]
    basic_5 = [(c.basic_5_leader)for c in Team_capability_fi.query.all()]
    suma_basic = sum(basic_1 + basic_2 + basic_3 + basic_4 + basic_5)
    largo_basic_1 = len(basic_1)
    maximo_basic = largo_basic_1 * 20
    #total_basic = suma_basic * 100 / 100
    total_basic = (suma_basic * 100) / maximo_basic 
    # PORCENTAJE LOSS INTELLIGENCE
    intelligence_1 = [(c.intelligence_1_leader)for c in Team_capability_fi.query.all()]
    intelligence_2 = [(c.intelligence_2_leader)for c in Team_capability_fi.query.all()]
    intelligence_3 = [(c.intelligence_3_leader)for c in Team_capability_fi.query.all()]
    intelligence_4 = [(c.intelligence_4_leader)for c in Team_capability_fi.query.all()]
    intelligence_5 = [(c.intelligence_5_leader)for c in Team_capability_fi.query.all()]
    suma_intelligence = sum(intelligence_1 + intelligence_2 + intelligence_3 + intelligence_4 + intelligence_5)
    largo_intelligence_1 = len(intelligence_1)
    maximo_intelligence = largo_intelligence_1 * 20
    #total_intelligence = suma_intelligence * 100 / 100
    total_intelligence = (suma_intelligence * 100) / maximo_intelligence
    # PORCENTAJE LOSS ERADICATION
    eradication_1 = [(c.eradication_1_leader)for c in Team_capability_fi.query.all()]
    eradication_2 = [(c.eradication_2_leader)for c in Team_capability_fi.query.all()]
    eradication_3 = [(c.eradication_3_leader)for c in Team_capability_fi.query.all()]
    eradication_4 = [(c.eradication_4_leader)for c in Team_capability_fi.query.all()]
    eradication_5 = [(c.eradication_5_leader)for c in Team_capability_fi.query.all()]
    eradication_6 = [(c.eradication_6_leader)for c in Team_capability_fi.query.all()]
    eradication_7 = [(c.eradication_7_leader)for c in Team_capability_fi.query.all()]
    suma_eradication = sum(eradication_1 + eradication_2 + eradication_3 + eradication_4 + eradication_5 + eradication_6 + eradication_7)
    largo_eradication_1 = len(eradication_1)
    maximo_eradication = largo_eradication_1 * 28
    #total_eradication = suma_eradication * 100 / 140
    total_eradication = (suma_eradication * 100) / maximo_eradication
    # PORCENTAJE LOSS PREVENTION
    prevention_1 = [(c.prevention_1_leader)for c in Team_capability_fi.query.all()]
    prevention_2 = [(c.prevention_2_leader)for c in Team_capability_fi.query.all()]
    prevention_3 = [(c.prevention_3_leader)for c in Team_capability_fi.query.all()]
    prevention_4 = [(c.prevention_4_leader)for c in Team_capability_fi.query.all()]
    prevention_5 = [(c.prevention_5_leader)for c in Team_capability_fi.query.all()]
    suma_prevention = sum(prevention_1 + prevention_2 + prevention_3 + prevention_4 + prevention_5)
    largo_prevention_1 = len(prevention_1)
    maximo_prevention = largo_prevention_1 * 20
    #total_prevention = suma_prevention * 100 / 100
    total_prevention = (suma_prevention * 100) / maximo_prevention
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    id = '1'
    paros = Teamcapability_fi.query.get(id)
    if id == '1':
        paros = Teamcapability_fi.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_fi.query.filter_by(Teamcapability_fiId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_fi.query.all()
    return render_template("Team_capability/team-capability.html", paros=paros, promedio_acreditacion=promedio_acreditacion,
                            promedio_calificacion=promedio_calificacion, form=form, comentario=comentario,
    total_basic=total_basic, total_intelligence=total_intelligence, total_prevention=total_prevention, total_eradication=total_eradication)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_tcapability_edit(id):
    from models.models_team_capability import Teamcapability_fi, Team_capability_fi, db
    dato = Team_capability_fi.query.all()
    dato_2 = [(c.basic_1_leader, c.basic_2_leader, c.basic_3_leader, c.basic_4_leader, c.basic_5_leader) for c in Team_capability_fi.query.filter_by(id=id).all()]
    # PORCENTAJE BASIC CONCEPT
    basic_1 = [(c.basic_1_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    basic_2 = [(c.basic_2_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    basic_3 = [(c.basic_3_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    basic_4 = [(c.basic_4_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    basic_5 = [(c.basic_5_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    suma_basic = sum(basic_1 + basic_2 + basic_3 + basic_4 + basic_5)
    total_basic = suma_basic * 100 / 20
    # PORCENTAJE LOSS INTELLIGENCE
    intelligence_1 = [(c.intelligence_1_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    intelligence_2 = [(c.intelligence_2_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    intelligence_3 = [(c.intelligence_3_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    intelligence_4 = [(c.intelligence_4_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    intelligence_5 = [(c.intelligence_5_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    suma_intelligence = sum(intelligence_1 + intelligence_2 + intelligence_3 + intelligence_4 + intelligence_5)
    total_intelligence = suma_intelligence * 100 / 20
    # PORCENTAJE LOSS ERADICATION
    eradication_1 = [(c.eradication_1_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    eradication_2 = [(c.eradication_2_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    eradication_3 = [(c.eradication_3_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    eradication_4 = [(c.eradication_4_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    eradication_5 = [(c.eradication_5_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    eradication_6 = [(c.eradication_6_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    eradication_7 = [(c.eradication_7_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    suma_eradication = sum(eradication_1 + eradication_2 + eradication_3 + eradication_4 + eradication_5 + eradication_6 + eradication_7)
    total_eradication = suma_eradication * 100 / 28
    # PORCENTAJE LOSS PREVENTION
    prevention_1 = [(c.prevention_1_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    prevention_2 = [(c.prevention_2_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    prevention_3 = [(c.prevention_3_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    prevention_4 = [(c.prevention_4_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    prevention_5 = [(c.prevention_5_leader)for c in Team_capability_fi.query.filter_by(id=id).all()]
    suma_prevention = sum(prevention_1 + prevention_2 + prevention_3 + prevention_4 + prevention_5)
    total_prevention = suma_prevention * 100 / 20
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_fi.query.get(id)
    ark = Team_capability_fi.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_fi(obj=art)
    form_2 = FormTeam_capability_fi(obj=ark)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        form_2.populate_obj(ark)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcapability"))
    return render_template("Team_capability/tcapability_edit.html", form=form, form_2=form_2, dato=dato, dato_2=dato_2,
    total_basic=total_basic, total_intelligence=total_intelligence, total_prevention=total_prevention, total_eradication=total_eradication)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-capability/new', methods=["get", "post"])
@login_required
def tablero_fi_tcapability_new():
    from models.models_team_capability import Teamcapability_fi, Team_capability_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormTeamcapability_fi()
    form_2 = FormTeam_capability_fi()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Teamcapability_fi()
        ark = Team_capability_fi(basic_1=0, basic_2=0, basic_3=0, basic_4=0, basic_5=0, intelligence_1=0, intelligence_2=0, intelligence_3=0,
        intelligence_4=0, intelligence_5=0, eradication_1=0, eradication_2=0, eradication_3=0, eradication_4=0, eradication_5=0, eradication_6=0,
        eradication_7=0, prevention_1=0, prevention_2=0, prevention_3=0, prevention_4=0, prevention_5=0, basic_1_leader=0, basic_2_leader=0, 
        basic_3_leader=0, basic_4_leader=0, basic_5_leader=0, intelligence_1_leader=0, intelligence_2_leader=0, intelligence_3_leader=0,
        intelligence_4_leader=0, intelligence_5_leader=0, eradication_1_leader=0, eradication_2_leader=0, eradication_3_leader=0, 
        eradication_4_leader=0, eradication_5_leader=0, eradication_6_leader=0, eradication_7_leader=0, prevention_1_leader=0, 
        prevention_2_leader=0, prevention_3_leader=0, prevention_4_leader=0, prevention_5_leader=0)
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        form.populate_obj(ark)
        db.session.add(art)
        db.session.add(ark)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcapability"))
    else:
        return render_template("Team_capability/tcapability_new.html", form=form, form_2=form_2)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-capability/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_tcapability_delete(id):
    from models.models_team_capability import Teamcapability_fi, Team_capability_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Teamcapability_fi.query.get(id)
    cats = Team_capability_fi.query.get(id)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.delete(cats)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcapability"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat, cats=cats)

###============================================ CBN LINK ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/cbn', methods=["get", "post"])
@login_required
def tablero_fi_cbn():
    from models.models_cbn import Cbn_fi, db
    from models.models_mission_vision import Mission_fi, db
    from models.models import Auditor_comentario, db
    id = '2'
    articulos = Mission_fi.query.filter_by(id=id)
    dato = Cbn_fi.query.all()
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[1:2]
    # COMENTARIO EDIT
    id = '2'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_cbn"))
    return render_template("Cbn_link/cbn-link.html", articulos=articulos, dato=dato, form=form, comentario=comentario)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_cbn_edit(id):
    from models.models_cbn import Cbn_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Cbn_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_cbn"))
    return render_template("Cbn_link/cbn-link_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/cbn/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_cbn_delete(id):
    from models.models_cbn import Cbn_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Cbn_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_cbn"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/cbn/new', methods=["get", "post"])
@login_required
def tablero_fi_cbn_new():
    from models.models_cbn import Cbn_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormCbn_fi()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cbn_fi()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_cbn"))
    else:
        return render_template("Cbn_link/cbn-link_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/cbn/<id>/edit/photo', methods=["get", "post"])
@login_required
def tablero_fi_cbn_edit_photo(id):
    from models.models_mission_vision import Mission_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    art = Mission_fi.query.get(id)
    if art is None:
        abort(404)
    form = FormMission_fi(obj=art)
    if form.validate_on_submit():
        # Borramos la imagen anterior si hemos subido una nueva
        if form.photo.data:
            os.remove(app.root_path+'/static/upload/'+art.image)
            try:
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + '/static/upload/' + nombre_fichero)
            except:
                nombre_fichero = ''
        else:
            nombre_fichero = art.image
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_cbn"))
    return render_template("Cbn_link/cbn-link_edit_photo.html", form=form)

###============================================ TEAM CHARTER ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-charter', methods=["get", "post"])
@login_required
def tablero_fi_tcharter():
    from models.models_team_charter import Teamcharter_fi, Teamcharter_comite_fi, db
    from models.models import Auditor_comentario, db
    dato = Teamcharter_fi.query.all()
    dato_comite = Teamcharter_comite_fi.query.all()
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[6:7]
    # COMENTARIO EDIT
    id = '7'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcharter"))
    return render_template("Team_charter/team-charter.html", dato=dato, form=form, comentario=comentario, dato_comite=dato_comite)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-charter/new', methods=["get", "post"])
@login_required
def tablero_fi_tcharter_new():
    from models.models_team_charter import Teamcharter_fi, Teamcharter_comite_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormTeamcharter_comite_fi(request.form)
    if form.validate_on_submit():
        cat = Teamcharter_comite_fi(miembro=form.miembro.data, area=form.area.data, rol=form.rol.data, sistema=form.sistema.data, 
                            firma=form.firma.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcharter"))
    else:
        return render_template("Team_charter/team-charter_new.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-charter/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_tcharter_edit(id):
    from models.models_team_charter import Teamcharter_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Teamcharter_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormTeamcharter_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcharter"))
    return render_template("Team_charter/team-charter_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-charter/<id>/edit_comite', methods=["get", "post"])
@login_required
def tablero_fi_tcharter_edit_comite(id):
    from models.models_team_charter import Teamcharter_comite_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Teamcharter_comite_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormTeamcharter_comite_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcharter"))
    return render_template("Team_charter/team-charter_new.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/team-charter/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_tcharter_delete(id):
    from models.models_team_charter import Teamcharter_comite_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Teamcharter_comite_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_tcharter"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ SOCORECARD ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/scorecard', methods=["get", "post"])
@login_required
def tablero_fi_scorecard():
    from models.models_scorecard import Scorecard_fi
    from models.models import Auditor_comentario, db
    dato = Scorecard_fi.query.all()
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[10:11]
    # COMENTARIO EDIT
    id = '11'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_scorecard"))
    return render_template("Scorecard/scorecard.html", dato=dato, form=form, comentario=comentario)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/scorecard/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_scorecard_edit(id):
    from models.models_scorecard import Scorecard_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Scorecard_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormScorecard_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_scorecard"))
    return render_template("Scorecard/scorecard_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/scorecard/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_scorecard_delete(id):
    from models.models_scorecard import Scorecard_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Scorecard_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_scorecard"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/scorecard/new', methods=["get", "post"])
@login_required
def tablero_fi_scorecard_new():
    from models.models_scorecard import Scorecard_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormScorecard_fi()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Scorecard_fi()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_scorecard"))
    else:
        return render_template("Scorecard/scorecard_edit.html", form=form)
###============================================ ONE PAGER ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/one-pager', methods=["get", "post"])
@login_required
def tablero_fi_onepager():
    from models.models_onepager import Onepager_fi
    from models.models import Auditor_comentario, db
    from models.models_team_capability import Teamcapability_fi, Team_capability_fi, db
    paros = Teamcapability_fi.query.all()
    dato_consulta = Onepager_fi.query.all()
    #dato = Onepager_fi.query.first()
    dato = Onepager_fi.query.order_by(Onepager_fi.id.desc()).first()
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[7:8]
    # COMENTARIO EDIT
    id = '8'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_onepager"))
    return render_template("One_pager/one-pager.html", dato=dato, form=form, comentario=comentario, dato_consulta=dato_consulta,
    paros=paros)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/one-pager/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_onepager_edit(id):
    from models.models_onepager import Onepager_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Onepager_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormOnepager_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_onepager"))
    return render_template("One_pager/one-pager_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/one-pager/new', methods=["get", "post"])
@login_required
def tablero_fi_onepager_new():
    from models.models_onepager import Onepager_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormOnepager_fi()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Onepager_fi()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_onepager"))
    else:
        return render_template("One_pager/one-pager_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/one-pager/<id>/view', methods=["get", "post"])
@login_required
def tablero_fi_onepager_view(id):
    from models.models_onepager import Onepager_fi, db
    from models.models_team_capability import Teamcapability_fi, Team_capability_fi, db
    paros = Teamcapability_fi.query.all()
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    dato = Onepager_fi.query.get(id)
    return render_template("One_pager/one-pager_view.html", dato=dato, paros=paros)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/one-pager/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_onepager_delete(id):
    from models.models_onepager import Onepager_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Onepager_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_onepager"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ PILLAR LOSS MAP ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-loss', methods=["get", "post"])
@login_required
def tablero_fi_pilarloss():
    from models.models_pilarlossmap import Pilarlossmap_fi
    from models.models import Auditor_comentario, db
    from models.models_mission_vision import Mission_fi, db
    id = '4'
    articulos = Mission_fi.query.filter_by(id=id)
    pilar = Pilarlossmap_fi.query.all()
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[3:4]
    # COMENTARIO EDIT
    id = '4'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarloss"))
    return render_template("Pillar_loss/pilar-loss.html", articulos=articulos, pilar=pilar, form=form, comentario=comentario)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-loss/<id>/edit/photo', methods=["get", "post"])
@login_required
def tablero_fi_pilarloss_edit_photo(id):
    from models.models_mission_vision import Mission_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    art = Mission_fi.query.get(id)
    if art is None:
        abort(404)
    form = FormMission_fi(obj=art)
    if form.validate_on_submit():
        # Borramos la imagen anterior si hemos subido una nueva
        if form.photo.data:
            os.remove(app.root_path+'/static/upload/'+art.image)
            try:
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + '/static/upload/' + nombre_fichero)
            except:
                nombre_fichero = ''
        else:
            nombre_fichero = art.image
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarloss"))
    return render_template("Pillar_loss/pilar-loss_edit_photo.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-loss/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_pilarloss_edit(id):
    from models.models_pilarlossmap import Pilarlossmap_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    pilar = Pilarlossmap_fi.query.get(id)
    if pilar is None:
        abort(404)
    form = FormPilarlossmap_fi(request.form, obj=pilar)
    if form.validate_on_submit():
        form.populate_obj(pilar)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarloss"))
    return render_template("Pillar_loss/pilar-loss_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-loss/new', methods=["get", "post"])
@login_required
def tablero_fi_pilarloss_new():
    from models.models_pilarlossmap import Pilarlossmap_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormPilarlossmap_fi(request.form)
    if form.validate_on_submit():
        cat = Pilarlossmap_fi(tema=form.tema.data, fecha=form.fecha.data,
                           responsable=form.responsable.data, objetivo=form.objetivo.data, estadoactual=form.estadoactual.data,
                           estadofuturo=form.estadofuturo.data, planesdeaccion=form.planesdeaccion.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarloss"))
    else:
        return render_template("Pillar_loss/pilar-loss_new.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/pilar-loss/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_pilarloss_delete(id):
    from models.models_pilarlossmap import Pilarlossmap_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Pilarlossmap_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_pilarloss"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ MASTER PLAN 3 AÑOS ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/master-plan', methods=["get", "post"])
@login_required
def tablero_fi_masterplan():
    from models.models_masterplan import Masterplan_fi, db
    from models.models import Auditor_comentario, db
    dato = Masterplan_fi.query.all()
    # COMENTARIO
    comentario = Auditor_comentario.query.all()[4:5]
    # COMENTARIO EDIT
    id = '5'
    comment = Auditor_comentario.query.get(id)
    if comment is None:
        abort(404)
    form = FormAuditor_comentario(obj=comment)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(comment)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_masterplan"))
    return render_template("Master_plan/master-plan.html", dato=dato, form=form, comentario=comentario)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/master-plan/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_masterplan_edit(id):
    from models.models_masterplan import Masterplan_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Masterplan_fi.query.get(id)
    if dato is None:
        abort(404)
    form = FormMasterplan_fi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_masterplan"))
    return render_template("Master_plan/master-plan_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/master-plan/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_masterplan_delete(id):
    from models.models_masterplan import Masterplan_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Masterplan_fi.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_masterplan"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/master-plan/new', methods=["get", "post"])
@login_required
def tablero_fi_masterplan_new():
    from models.models_masterplan import Masterplan_fi, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormMasterplan_fi()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Masterplan_fi()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_masterplan"))
    else:
        return render_template("Master_plan/master-plan_edit.html", form=form)
###============================================ GAP ANALISIS 1 ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis1', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_1():
    from models.models_gap_analisis import Gapanalisis_fi_1, Gapanalisis_fi_1_efecto, db
    dato = Gapanalisis_fi_1.query.all()
    dato_2 = Gapanalisis_fi_1_efecto.query.all()
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_1_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_1_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_1"))
    else:
        return render_template("Gap_analisis/1/gap-analysis-1.html", dato=dato, form=form, dato_2=dato_2)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis1/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_1_edit(id):
    from models.models_gap_analisis import Gapanalisis_fi_1, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_1.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_1(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_1"))
    return render_template("Gap_analisis/1/gap-analysis-1_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis1/efecto/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_1_edit_efecto(id):
    from models.models_gap_analisis import Gapanalisis_fi_1, Gapanalisis_fi_1_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_1_efecto.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_1_efecto(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_1"))
    return render_template("Gap_analisis/1/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis1/efecto/new', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_1_new_efecto():
    from models.models_gap_analisis import Gapanalisis_fi_1, Gapanalisis_fi_1_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_1_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_1_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_1"))
    else:
        return render_template("Gap_analisis/1/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis1/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_1_delete(id):
    from models.models_gap_analisis import Gapanalisis_fi_1_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Gapanalisis_fi_1_efecto.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_1"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ GAP ANALISIS 2 ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis2', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_2():
    from models.models_gap_analisis import Gapanalisis_fi_2, Gapanalisis_fi_2_efecto, db
    dato = Gapanalisis_fi_2.query.all()
    dato_2 = Gapanalisis_fi_2_efecto.query.all()
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_2_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_2_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_2"))
    else:
        return render_template("Gap_analisis/2/gap-analysis-1.html", dato=dato, form=form, dato_2=dato_2)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis2/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_2_edit(id):
    from models.models_gap_analisis import Gapanalisis_fi_2, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_2.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_2(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_2"))
    return render_template("Gap_analisis/2/gap-analysis-1_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis2/efecto/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_2_edit_efecto(id):
    from models.models_gap_analisis import Gapanalisis_fi_2, Gapanalisis_fi_2_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_2_efecto.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_2_efecto(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_2"))
    return render_template("Gap_analisis/2/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis2/efecto/new', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_2_new_efecto():
    from models.models_gap_analisis import Gapanalisis_fi_2, Gapanalisis_fi_2_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_2_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_2_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_2"))
    else:
        return render_template("Gap_analisis/2/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis2/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_2_delete(id):
    from models.models_gap_analisis import Gapanalisis_fi_2_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Gapanalisis_fi_2_efecto.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_2"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ GAP ANALISIS 3 ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis3', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_3():
    from models.models_gap_analisis import Gapanalisis_fi_3, Gapanalisis_fi_3_efecto, db
    dato = Gapanalisis_fi_3.query.all()
    dato_2 = Gapanalisis_fi_3_efecto.query.all()
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_3_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_3_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_3"))
    else:
        return render_template("Gap_analisis/3/gap-analysis-1.html", dato=dato, form=form, dato_2=dato_2)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis3/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_3_edit(id):
    from models.models_gap_analisis import Gapanalisis_fi_3, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_3.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_3(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_3"))
    return render_template("Gap_analisis/3/gap-analysis-1_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis3/efecto/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_3_edit_efecto(id):
    from models.models_gap_analisis import Gapanalisis_fi_3, Gapanalisis_fi_3_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_3_efecto.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_3_efecto(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_3"))
    return render_template("Gap_analisis/3/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis3/efecto/new', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_3_new_efecto():
    from models.models_gap_analisis import Gapanalisis_fi_3, Gapanalisis_fi_3_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_3_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_3_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_3"))
    else:
        return render_template("Gap_analisis/3/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis3/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_3_delete(id):
    from models.models_gap_analisis import Gapanalisis_fi_3_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Gapanalisis_fi_3_efecto.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_3"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ GAP ANALISIS 4 ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis4', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_4():
    from models.models_gap_analisis import Gapanalisis_fi_4, Gapanalisis_fi_4_efecto, db
    dato = Gapanalisis_fi_4.query.all()
    dato_2 = Gapanalisis_fi_4_efecto.query.all()
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_4_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_4_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_4"))
    else:
        return render_template("Gap_analisis/4/gap-analysis-1.html", dato=dato, form=form, dato_2=dato_2)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis4/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_4_edit(id):
    from models.models_gap_analisis import Gapanalisis_fi_4, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_4.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_4(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_4"))
    return render_template("Gap_analisis/4/gap-analysis-1_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis4/efecto/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_4_edit_efecto(id):
    from models.models_gap_analisis import Gapanalisis_fi_4, Gapanalisis_fi_4_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_4_efecto.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_4_efecto(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_4"))
    return render_template("Gap_analisis/4/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis4/efecto/new', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_4_new_efecto():
    from models.models_gap_analisis import Gapanalisis_fi_4, Gapanalisis_fi_4_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_4_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_4_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_4"))
    else:
        return render_template("Gap_analisis/4/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis4/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_4_delete(id):
    from models.models_gap_analisis import Gapanalisis_fi_4_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Gapanalisis_fi_4_efecto.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_4"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ GAP ANALISIS 5 ====================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis5', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_5():
    from models.models_gap_analisis import Gapanalisis_fi_5, Gapanalisis_fi_5_efecto, db
    dato = Gapanalisis_fi_5.query.all()
    dato_2 = Gapanalisis_fi_5_efecto.query.all()
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_5_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_5_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_5"))
    else:
        return render_template("Gap_analisis/5/gap-analysis-1.html", dato=dato, form=form, dato_2=dato_2)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis5/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_5_edit(id):
    from models.models_gap_analisis import Gapanalisis_fi_5, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_5.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_5(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_5"))
    return render_template("Gap_analisis/5/gap-analysis-1_edit.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis5/efecto/<id>/edit', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_5_edit_efecto(id):
    from models.models_gap_analisis import Gapanalisis_fi_5, Gapanalisis_fi_5_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    dato = Gapanalisis_fi_5_efecto.query.get(id)
    if dato is None:
        abort(404)
    form = FormGapanalisis_fi_5_efecto(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_5"))
    return render_template("Gap_analisis/5/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis5/efecto/new', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_5_new_efecto():
    from models.models_gap_analisis import Gapanalisis_fi_5, Gapanalisis_fi_5_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    form = FormGapanalisis_fi_5_efecto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Gapanalisis_fi_5_efecto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_5"))
    else:
        return render_template("Gap_analisis/5/gap-analysis-1_edit_efecto.html", form=form)

@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/gap-analisis5/<id>/delete', methods=["get", "post"])
@login_required
def tablero_fi_gapanalisis_5_delete(id):
    from models.models_gap_analisis import Gapanalisis_fi_5_efecto, db
    # Control de permisos
    if not current_user.is_user_fi() and current_user.is_admin():
        abort(404)
    cat = Gapanalisis_fi_5_efecto.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("pizarron_fi.tablero_fi_gapanalisis_5"))
    return render_template("Pillar_loss/pilar-loss_delete.html", form=form, cat=cat)

###============================================ RECONOCIMIENTO ========================================================###
@pizarron_fi.route('/menu/inicio/pilares_il6s/FI_menu/tablero/reconocimiento_interno')
@login_required
def tablero_fi_reconocimiento_interno():
    from models.models_organigrama import Organigrama_fi
        # Reconociemnto
    todo = Organigrama_fi.query.all()[1:]
    lider = Organigrama_fi.query.all()[0:1]
    return render_template("Reconocimiento_interno/reconocimiento_interno.html", todo=todo, lider=lider)
###============================================ FIN RECONOCIMIENTO ====================================================###
