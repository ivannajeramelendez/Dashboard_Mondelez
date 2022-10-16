from flask import Flask, render_template, redirect, url_for, request, abort,\
    session, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

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

app = Flask(__name__)

pizarron_qm = Blueprint('pizarron_qm', __name__)

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu')
@login_required
def menu_pilares_qm():
    return render_template("pilares/QM/menu_pilares_qm.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero')
@login_required
def tablero_qm():
    return render_template("tableros/tablero_qm.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/mision')
@login_required
def tablero_qm_mission():
    return render_template("pizarron/QM/mission.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/organigrama')
@login_required
def tablero_qm_organigrama():
    return render_template("pizarron/QM/organigrama-pilar.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/cbn')
@login_required
def tablero_qm_cbn():
    from models.models_cbn import Cbn_qm
    dato = Cbn_qm.query.all()
    return render_template("pizarron/QM/cbn-link.html", dato=dato)

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_qm_cbn_edit(id):
    from models.models_cbn import Cbn_qm, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_qm.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_qm(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_qm.tablero_qm_cbn"))
    return render_template("pizarron/QM/cbn-link_edit.html", form=form)

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/team-capability')
@login_required
def tcapability_qm(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_qm
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_qm.query.get(id)
    if id == '1':
        paros = Teamcapability_qm.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_qm.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_qm.query.all()
    return render_template("pizarron/QM/team-capability.html", paros=paros)

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_qm(id):
    from models.models_team_capability import Teamcapability_qm, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_qm.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_qm(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_qm.tcapability_qm"))
    return render_template("pizarron/QM/tcapability_edit.html", form=form)

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/grafica-capability')
@login_required
def tablero_qm_capability():
    return render_template("pizarron/QM/grafica-capability.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/pilar-swot')
@login_required
def tablero_qm_plar_swot():
    return render_template("pizarron/QM/pilar-swot.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/plan-90-dias')
@login_required
def tablero_qm_plan_90():
    return render_template("pizarron/QM/90-dias.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_qm_sistemas_herramienta():
    return render_template("pizarron/QM/grafica-sistemas-herramienta.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/status-loss')
@login_required
def tablero_qm_status_loss():
    return render_template("pizarron/QM/estatus-perdidas.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/gap-analisis2')
@login_required
def tablero_qm_gapanalisis_2():
    return render_template("pizarron/QM/gap-analysis-2.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/gap-analisis3')
@login_required
def tablero_qm_gapanalisis_3():
    return render_template("pizarron/QM/gap-analysis-3.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/gap-analisis4')
@login_required
def tablero_qm_gapanalisis_4():
    return render_template("pizarron/QM/gap-analysis-4.html")

@pizarron_qm.route('/menu/inicio/pilares_il6s/QM_menu/tablero/gap-analisis5')
@login_required
def tablero_qm_gapanalisis_5():
    return render_template("pizarron/QM/gap-analysis-5.html")