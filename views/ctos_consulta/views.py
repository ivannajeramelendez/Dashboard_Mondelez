from flask import Flask, render_template, redirect, url_for, request, abort,\
    session, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, column, table, select, asc, bindparam
import os
    # FORMULARIOS
from forms.forms import *
from forms.forms_fi import *
from forms.forms_am import *
from forms.forms_eyt import *
from forms.forms_iim import *
from forms.forms_lead import *
from forms.forms_hse import *
from forms.forms_org import *
from forms.forms_pm import *
from forms.forms_qm import *
from forms.forms_sn import *
from forms.forms_wpi import *
from forms.forms_ctos_edit import *

app = Flask(__name__)

ctos_consulta = Blueprint('ctos_consulta', __name__, template_folder='templates', static_folder='static')

# 1'S ====================================================================================================== #
@ctos_consulta.route('/menu/inicio/ctos/Slab1s/consulta/graph')
@login_required
def cto_consulta_slab_1s_graph(id='0'):
    from models.models import Cto1s_bosch_1, Ctofallas, Sku, Lineas, Areas
    # OPERACIONES
        # Fallas Cto
    #lista_fallas = [(c.falla) for c in Ctofallas.query.all()[0:]]
    #busqueda = Cto1s_bosch_1.query.order_by(Cto1s_bosch_1.fecha).all()
        # Ge
    lista_ge = ((c.ge)for c in Cto1s_bosch_1.query.all())
    suma_ge = [lista for lista in lista_ge]
    largo_ge = len(suma_ge)
    total_ge = sum(suma_ge)
    cambio_ge =  (total_ge / largo_ge ) / 100 * 100
    resul_ge = ("{:.2f}".format(cambio_ge))
    planned = 100 - cambio_ge
    no_planned = 100 - cambio_ge
        # Frecuencia fallas
    lista_frec = ((c.frec)for c in Cto1s_bosch_1.query.all())
    suma_frec = [lista for lista in lista_frec]
    total_frec = sum(suma_frec)
    # Consultas
    lineas = Lineas.query.all()[1:]
    fallas = Cto1s_bosch_1.query.all()[0:]
    areas = Areas.query.all()[1:]

    # Tabla
    paros = Cto1s_bosch_1.query.all()
    return render_template("Slab_1s/cto_slab_1s_consulta.html", fallas=fallas, lineas=lineas, areas=areas, resul_ge=resul_ge, 
    no_planned=no_planned, paros=paros, planned=planned, total_frec=total_frec)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_1s/')
@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_1s/<id>')
@login_required
def cto_consulta_slab_1s_registros(id='0'):
    from models.models import Cto1s_bosch_1, Ctofallas, Sku, Lineas, Areas, db
    # SE LLAMA LA VARIABLE DE LA TABLA
    areas = Areas.query.get(id)
    if id == '0':
        registro = Cto1s_bosch_1.query.all()
    else:
        registro = Cto1s_bosch_1.query.filter_by(RegistroId=id)
    areas = Areas.query.all()    
    return render_template("Resultados/slab_1s/vista_resultados.html", registro=registro, areas=areas)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_1s/<id>/view', methods=["get", "post"])
@login_required
def cto_consulta_slab_1s_registros_view(id):
    from models.models import Cto1s_bosch_1, Ctofallas, Sku, Lineas, Areas, Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Cto1s_bosch_1.query.get(id)
    # Formulario para editar
    cat = Cto1s_bosch_1.query.get(id)
    if cat is None:
        abort(404)
    form = FormCto1s_prototipo_edit(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("Resultados/slab_1s/vista_resultados_id.html", form=form, slab_cto=slab_cto)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_1s/Bosch/<id>/view', methods=["get", "post"])
@login_required
def cto_consulta_slab_1s_bosch_2_registros_view(id):
    from models.models import Cto1s_bosch_2, Ctofallas, Sku, Lineas, Areas, Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Cto1s_bosch_2.query.get(id)
    # Formulario para editar
    cat = Cto1s_bosch_2.query.get(id)
    if cat is None:
        abort(404)
    form = FormCto1s_bosch_2_edit(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("Resultados/slab_1s/vista_resultados_id.html", form=form, slab_cto=slab_cto)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_1s/<id>/delete', methods=["get", "post"])
@login_required
def cto_consulta_slab_1s_registros_delete(id):
    from models.models import Cto1s_bosch_1, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Cto1s_bosch_1.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("delete_elemento.html", form=form, cat=cat)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_1s/Bosch_2/<id>/delete', methods=["get", "post"])
@login_required
def cto_consulta_slab_1s_bosch_2_registros_delete(id):
    from models.models import Cto1s_bosch_2, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Cto1s_bosch_2.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("delete_elemento.html", form=form, cat=cat)
# 6'S ====================================================================================================== #
@ctos_consulta.route('/menu/inicio/ctos/Slab6s/consulta/graph')
@login_required
def cto_consulta_slab_6s_graph(id='1'):
    from models.models import Cto6s_prototipo_l1, Cto6s_prototipo_l2, Cto6s_prototipo_l3, Cto6s_prototipo_l4,\
        Ctofallas, Sku, Lineas, Areas
    # OPERACIONES
        # Ge consulta de resultados
    lista_ge = ((c.ge)for c in Cto6s_prototipo_l1.query.all())
    suma_ge = [lista for lista in lista_ge]
    lista_l2 = ((c.ge)for c in Cto6s_prototipo_l2.query.all())
    suma_l2 = [lista for lista in lista_l2]
    lista_l3 = ((c.ge)for c in Cto6s_prototipo_l3.query.all())
    suma_l3 = [lista for lista in lista_l3]
    lista_l4 = ((c.ge)for c in Cto6s_prototipo_l4.query.all())
    suma_l4 = [lista for lista in lista_l4]
        # Operacion con los resultados
    largo_ge = len(suma_ge + suma_l2 + suma_l3 + suma_l4)
    total_ge = sum(suma_ge + suma_l2 + suma_l3 + suma_l4)
    cambio_ge =  (total_ge / largo_ge ) / 100 * 100
    resul_ge = ("{:.2f}".format(cambio_ge))
    planned = 100 - cambio_ge
    no_planned = 100 - cambio_ge
        # Frecuencia fallas
    lista_frec = ((c.frec)for c in Cto6s_prototipo_l1.query.all())
    suma_frec = [lista for lista in lista_frec]
    lista_frec_l2 = ((c.frec)for c in Cto6s_prototipo_l2.query.all())
    suma_frec_l2 = [lista for lista in lista_frec_l2]
    lista_frec_l3 = ((c.frec)for c in Cto6s_prototipo_l3.query.all())
    suma_frec_l3 = [lista for lista in lista_frec_l3]
    lista_frec_l4 = ((c.frec)for c in Cto6s_prototipo_l4.query.all())
    suma_frec_l4 = [lista for lista in lista_frec_l4]
    total_frec = sum(suma_frec + suma_frec_l2 + suma_frec_l3 + suma_frec_l4)
    # Consultas
    lineas = Lineas.query.all()[1:]
    fallas = Cto6s_prototipo_l1.query.all()[0:]
    areas = Areas.query.all()[1:]
    # Tablas
    paros = Cto6s_prototipo_l1.query.all()
    linea_2 = Cto6s_prototipo_l2.query.all()
    linea_3 = Cto6s_prototipo_l3.query.all()
    linea_4 = Cto6s_prototipo_l4.query.all()
    return render_template("Slab_6s/cto_slab_6s_consulta.html", fallas=fallas, lineas=lineas, areas=areas, resul_ge=resul_ge, 
    no_planned=no_planned, paros=paros, planned=planned, total_frec=total_frec, linea_2=linea_2, linea_3=linea_3, linea_4=linea_4)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/')
@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>')
@login_required
def cto_consulta_slab_6s_registros(id='0'):
    from models.models import Cto6s_prototipo_l1, Cto6s_prototipo_l2, Cto6s_prototipo_l3, Cto6s_prototipo_l4,\
        Ctofallas, Sku, Lineas, Areas, db
    # SE LLAMA LA VARIABLE DE LA TABLA
    if id == '0':
        registro = Cto6s_prototipo_l1.query.all()
        registro_2 = Cto6s_prototipo_l2.query.all()
        registro_3 = Cto6s_prototipo_l3.query.all()
        registro_4 = Cto6s_prototipo_l4.query.all()
    else:
        registro = Cto6s_prototipo_l1.query.filter_by(RegistroId=id)
        registro_2 = Cto6s_prototipo_l2.query.filter_by(RegistroId=id)
        registro_3 = Cto6s_prototipo_l3.query.filter_by(RegistroId=id)
        registro_4 = Cto6s_prototipo_l4.query.filter_by(RegistroId=id)
    return render_template("Resultados/slab_6s/vista_resultados.html", registro=registro, registro_2=registro_2, 
    registro_3=registro_3, registro_4=registro_4)

# 6'S EDICION ====================================================================================================== #
@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/view/l1', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_view(id):
    from models.models import Cto6s_prototipo_l1, Ctofallas, Sku, Lineas, Areas, Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Cto6s_prototipo_l1.query.get(id)
    # Formulario para editar
    cat = Cto6s_prototipo_l1.query.get(id)
    if cat is None:
        abort(404)
    form = FormCto6s_prototipo_l1_edit(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("Resultados/slab_6s/vista_resultados_id.html", form=form, slab_cto=slab_cto)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/view/l2', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_view_l2(id):
    from models.models import Cto6s_prototipo_l2, Ctofallas, Sku, Lineas, Areas, Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Cto6s_prototipo_l2.query.get(id)
    # Formulario para editar
    cat = Cto6s_prototipo_l2.query.get(id)
    if cat is None:
        abort(404)
    form = FormCto6s_prototipo_l2_edit(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("Resultados/slab_6s/vista_resultados_id.html", form=form, slab_cto=slab_cto)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/view/l3', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_view_l3(id):
    from models.models import Cto6s_prototipo_l3, Ctofallas, Sku, Lineas, Areas, Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Cto6s_prototipo_l3.query.get(id)
    # Formulario para editar
    cat = Cto6s_prototipo_l3.query.get(id)
    if cat is None:
        abort(404)
    form = FormCto6s_prototipo_l3_edit(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("Resultados/slab_6s/vista_resultados_id.html", form=form, slab_cto=slab_cto)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/view/l4', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_view_l4(id):
    from models.models import Cto6s_prototipo_l4, Ctofallas, Sku, Lineas, Areas, Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Cto6s_prototipo_l4.query.get(id)
    # Formulario para editar
    cat = Cto6s_prototipo_l4.query.get(id)
    if cat is None:
        abort(404)
    form = FormCto6s_prototipo_l4_edit(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("Resultados/slab_6s/vista_resultados_id.html", form=form, slab_cto=slab_cto)

# 6'S ELIMINACION ====================================================================================================== #
@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/delete/l1', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_delete(id):
    from models.models import Cto6s_prototipo_l1, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Cto6s_prototipo_l1.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("delete_elemento.html", form=form, cat=cat)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/delete/l2', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_delete_l2(id):
    from models.models import Cto6s_prototipo_l2, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Cto6s_prototipo_l2.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("delete_elemento.html", form=form, cat=cat)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/delete/l3', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_delete_l3(id):
    from models.models import Cto6s_prototipo_l3, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Cto6s_prototipo_l3.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("delete_elemento.html", form=form, cat=cat)

@ctos_consulta.route('/menu/inicio/ctos/consulta/resultado/Slab_6s/<id>/delete/l4', methods=["get", "post"])
@login_required
def cto_consulta_slab_6s_registros_delete_l4(id):
    from models.models import Cto6s_prototipo_l4, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Cto6s_prototipo_l4.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_consulta_capturas"))
    return render_template("delete_elemento.html", form=form, cat=cat)