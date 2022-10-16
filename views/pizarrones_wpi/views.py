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

pizarron_wpi = Blueprint('pizarron_wpi', __name__)

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu')
@login_required
def menu_pilares_wpi():
    return render_template("pilares/WPI/menu_pilares_wpi.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero')
@login_required
def tablero_wpi():
    return render_template("tableros/tablero_wpi.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/mision')
@login_required
def tablero_wpi_mission():
    return render_template("pizarron/WPI/mission.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/organigrama')
@login_required
def tablero_wpi_organigrama():
    return render_template("pizarron/WPI/organigrama-pilar.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/cbn')
@login_required
def tablero_wpi_cbn():
    from models.models_cbn import Cbn_wpi
    dato = Cbn_wpi.query.all()
    return render_template("pizarron/WPI/cbn-link.html", dato=dato)

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_wpi_cbn_edit(id):
    from models.models_cbn import Cbn_wpi, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_wpi.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_wpi(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_wpi.tablero_wpi_cbn"))
    return render_template("pizarron/WPI/cbn-link_edit.html", form=form)

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/team-capability')
@login_required
def tcapability_wpi(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_wpi
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_wpi.query.get(id)
    if id == '1':
        paros = Teamcapability_wpi.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_wpi.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_wpi.query.all()
    return render_template("pizarron/WPI/team-capability.html", paros=paros)

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_wpi(id):
    from models.models_team_capability import Teamcapability_wpi, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_wpi.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_wpi(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_wpi.tcapability_wpi"))
    return render_template("pizarron/WPI/tcapability_edit.html", form=form)

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/grafica-capability')
@login_required
def tablero_wpi_capability():
    return render_template("pizarron/WPI/grafica-capability.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/pilar-swot')
@login_required
def tablero_wpi_plar_swot():
    return render_template("pizarron/WPI/pilar-swot.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/plan-90-dias')
@login_required
def tablero_wpi_plan_90():
    return render_template("pizarron/WPI/90-dias.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_wpi_sistemas_herramienta():
    return render_template("pizarron/WPI/grafica-sistemas-herramienta.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/status-loss')
@login_required
def tablero_wpi_status_loss():
    return render_template("pizarron/WPI/estatus-perdidas.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/gap-analisis2')
@login_required
def tablero_wpi_gapanalisis_2():
    return render_template("pizarron/WPI/gap-analysis-2.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/gap-analisis3')
@login_required
def tablero_wpi_gapanalisis_3():
    return render_template("pizarron/WPI/gap-analysis-3.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/gap-analisis4')
@login_required
def tablero_wpi_gapanalisis_4():
    return render_template("pizarron/WPI/gap-analysis-4.html")

@pizarron_wpi.route('/menu/inicio/pilares_il6s/WPI_menu/tablero/gap-analisis5')
@login_required
def tablero_wpi_gapanalisis_5():
    return render_template("pizarron/WPI/gap-analysis-5.html")