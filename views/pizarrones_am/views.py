from flask import Flask, render_template, redirect, url_for, request, abort,\
    session, Response, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
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

app = Flask(__name__)

pizarron_am = Blueprint('pizarron_am', __name__)

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu')
@login_required
def menu_pilares_am():
    return render_template("pilares/AM/menu_pilares_am.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero')
@login_required
def tablero_am():
    return render_template("tableros/tablero_am.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/mision')
@login_required
def tablero_am_mission():
    return render_template("pizarron/AM/mission.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/organigrama')
@login_required
def tablero_am_organigrama():
    return render_template("pizarron/AM/organigrama-pilar.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/cbn')
@login_required
def tablero_am_cbn():
    from models.models_cbn import Cbn_am
    dato = Cbn_am.query.all()
    return render_template("pizarron/AM/cbn-link.html", dato=dato)

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_am_cbn_edit(id):
    from models.models_cbn import Cbn_am, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_am.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_am(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_am.tablero_am_cbn"))
    return render_template("pizarron/AM/cbn-link_edit.html", form=form)

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/team-capability')
@login_required
def tcapability_am(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_am
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_am.query.get(id)
    if id == '1':
        paros = Teamcapability_am.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_am.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_am.query.all()
    return render_template("pizarron/AM/team-capability.html", paros=paros)

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_am(id):
    from models.models_team_capability import Teamcapability_am, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_am.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_am(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_am.tcapability_am"))
    return render_template("pizarron/AM/tcapability_edit.html", form=form)

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/grafica-capability')
@login_required
def tablero_am_capability():
    return render_template("pizarron/AM/grafica-capability.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/pilar-swot')
@login_required
def tablero_am_plar_swot():
    return render_template("pizarron/AM/pilar-swot.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/plan-90-dias')
@login_required
def tablero_am_plan_90():
    return render_template("pizarron/AM/90-dias.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_am_sistemas_herramienta():
    return render_template("pizarron/AM/grafica-sistemas-herramienta.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/status-loss')
@login_required
def tablero_am_status_loss():
    return render_template("pizarron/AM/estatus-perdidas.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/gap-analisis2')
@login_required
def tablero_am_gapanalisis_2():
    return render_template("pizarron/AM/gap-analysis-2.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/gap-analisis3')
@login_required
def tablero_am_gapanalisis_3():
    return render_template("pizarron/AM/gap-analysis-3.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/gap-analisis4')
@login_required
def tablero_am_gapanalisis_4():
    return render_template("pizarron/AM/gap-analysis-4.html")

@pizarron_am.route('/menu/inicio/pilares_il6s/AM_menu/tablero/gap-analisis5')
@login_required
def tablero_am_gapanalisis_5():
    return render_template("pizarron/AM/gap-analysis-5.html")

