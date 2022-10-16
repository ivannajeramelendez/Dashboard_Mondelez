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

pizarron_eyt = Blueprint('pizarron_eyt', __name__)

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu')
@login_required
def menu_pilares_eyt():
    return render_template("pilares/E&T/menu_pilares_eyt.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero')
@login_required
def tablero_eyt():
    return render_template("tableros/tablero_eyt.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/mision')
@login_required
def tablero_eyt_mission():
    return render_template("pizarron/E&T/mission.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/organigrama')
@login_required
def tablero_eyt_organigrama():
    return render_template("pizarron/E&T/organigrama-pilar.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/cbn')
@login_required
def tablero_eyt_cbn():
    from models.models_cbn import Cbn_eyt
    dato = Cbn_eyt.query.all()
    return render_template("pizarron/E&T/cbn-link.html", dato=dato)

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_eyt_cbn_edit(id):
    from models.models_cbn import Cbn_eyt, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_eyt.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_eyt(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_eyt.tablero_eyt_cbn"))
    return render_template("pizarron/E&T/cbn-link_edit.html", form=form)

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/team-capability')
@login_required
def tcapability_eyt(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_eyt
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_eyt.query.get(id)
    if id == '1':
        paros = Teamcapability_eyt.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_eyt.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_eyt.query.all()
    return render_template("pizarron/E&T/team-capability.html", paros=paros)

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_eyt(id):
    from models.models_team_capability import Teamcapability_eyt, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_eyt.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_eyt(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_eyt.tcapability_eyt"))
    return render_template("pizarron/E&T/tcapability_edit.html", form=form)

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/grafica-capability')
@login_required
def tablero_eyt_capability():
    return render_template("pizarron/E&T/grafica-capability.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/pilar-swot')
@login_required
def tablero_eyt_plar_swot():
    return render_template("pizarron/E&T/pilar-swot.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/plan-90-dias')
@login_required
def tablero_eyt_plan_90():
    return render_template("pizarron/E&T/90-dias.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_eyt_sistemas_herramienta():
    return render_template("pizarron/E&T/grafica-sistemas-herramienta.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/status-loss')
@login_required
def tablero_eyt_status_loss():
    return render_template("pizarron/E&T/estatus-perdidas.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/gap-analisis2')
@login_required
def tablero_eyt_gapanalisis_2():
    return render_template("pizarron/E&T/gap-analysis-2.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/gap-analisis3')
@login_required
def tablero_eyt_gapanalisis_3():
    return render_template("pizarron/E&T/gap-analysis-3.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/gap-analisis4')
@login_required
def tablero_eyt_gapanalisis_4():
    return render_template("pizarron/E&T/gap-analysis-4.html")

@pizarron_eyt.route('/menu/inicio/pilares_il6s/E&T_menu/tablero/gap-analisis5')
@login_required
def tablero_eyt_gapanalisis_5():
    return render_template("pizarron/E&T/gap-analysis-5.html")