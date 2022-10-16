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

pizarron_pm = Blueprint('pizarron_pm', __name__)

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu')
@login_required
def menu_pilares_pm():
    return render_template("pilares/PM/menu_pilares_pm.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero')
@login_required
def tablero_pm():
    return render_template("tableros/tablero_pm.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/mision')
@login_required
def tablero_pm_mission():
    return render_template("pizarron/PM/mission.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/organigrama')
@login_required
def tablero_pm_organigrama():
    return render_template("pizarron/PM/organigrama-pilar.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/cbn')
@login_required
def tablero_pm_cbn():
    from models.models_cbn import Cbn_pm
    dato = Cbn_pm.query.all()
    return render_template("pizarron/PM/cbn-link.html", dato=dato)

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_pm_cbn_edit(id):
    from models.models_cbn import Cbn_pm, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_pm.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_pm(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_pm.tablero_pm_cbn"))
    return render_template("pizarron/PM/cbn-link_edit.html", form=form)

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/team-capability')
@login_required
def tcapability_pm(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_pm
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_pm.query.get(id)
    if id == '1':
        paros = Teamcapability_pm.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_pm.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_pm.query.all()
    return render_template("pizarron/PM/team-capability.html", paros=paros)

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_pm(id):
    from models.models_team_capability import Teamcapability_pm, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_pm.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_pm(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_pm.tcapability_pm"))
    return render_template("pizarron/PM/tcapability_edit.html", form=form)

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/grafica-capability')
@login_required
def tablero_pm_capability():
    return render_template("pizarron/PM/grafica-capability.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/pilar-swot')
@login_required
def tablero_pm_plar_swot():
    return render_template("pizarron/PM/pilar-swot.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/plan-90-dias')
@login_required
def tablero_pm_plan_90():
    return render_template("pizarron/PM/90-dias.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_pm_sistemas_herramienta():
    return render_template("pizarron/PM/grafica-sistemas-herramienta.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/status-loss')
@login_required
def tablero_pm_status_loss():
    return render_template("pizarron/PM/estatus-perdidas.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/gap-analisis2')
@login_required
def tablero_pm_gapanalisis_2():
    return render_template("pizarron/PM/gap-analysis-2.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/gap-analisis3')
@login_required
def tablero_pm_gapanalisis_3():
    return render_template("pizarron/PM/gap-analysis-3.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/gap-analisis4')
@login_required
def tablero_pm_gapanalisis_4():
    return render_template("pizarron/PM/gap-analysis-4.html")

@pizarron_pm.route('/menu/inicio/pilares_il6s/PM_menu/tablero/gap-analisis5')
@login_required
def tablero_pm_gapanalisis_5():
    return render_template("pizarron/PM/gap-analysis-5.html")