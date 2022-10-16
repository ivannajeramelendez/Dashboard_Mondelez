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

pizarron_org = Blueprint('pizarron_org', __name__)

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu')
@login_required
def menu_pilares_org():
    return render_template("pilares/ORG/menu_pilares_org.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero')
@login_required
def tablero_org():
    return render_template("tableros/tablero_org.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/mision')
@login_required
def tablero_org_mission():
    return render_template("pizarron/ORG/mission.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/organigrama')
@login_required
def tablero_org_organigrama():
    return render_template("pizarron/ORG/organigrama-pilar.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/cbn')
@login_required
def tablero_org_cbn():
    from models.models_cbn import Cbn_org
    dato = Cbn_org.query.all()
    return render_template("pizarron/ORG/cbn-link.html", dato=dato)

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_org_cbn_edit(id):
    from models.models_cbn import Cbn_org, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_org.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_org(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_org.tablero_org_cbn"))
    return render_template("pizarron/ORG/cbn-link_edit.html", form=form)

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/team-capability')
@login_required
def tcapability_org(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_org
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_org.query.get(id)
    if id == '1':
        paros = Teamcapability_org.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_org.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_org.query.all()
    return render_template("pizarron/ORG/team-capability.html", paros=paros)

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_org(id):
    from models.models_team_capability import Teamcapability_org, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_org.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_org(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_org.tcapability_org"))
    return render_template("pizarron/ORG/tcapability_edit.html", form=form)

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/grafica-capability')
@login_required
def tablero_org_capability():
    return render_template("pizarron/ORG/grafica-capability.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/pilar-swot')
@login_required
def tablero_org_plar_swot():
    return render_template("pizarron/ORG/pilar-swot.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/plan-90-dias')
@login_required
def tablero_org_plan_90():
    return render_template("pizarron/ORG/90-dias.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_org_sistemas_herramienta():
    return render_template("pizarron/ORG/grafica-sistemas-herramienta.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/status-loss')
@login_required
def tablero_org_status_loss():
    return render_template("pizarron/ORG/estatus-perdidas.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/gap-analisis2')
@login_required
def tablero_org_gapanalisis_2():
    return render_template("pizarron/ORG/gap-analysis-2.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/gap-analisis3')
@login_required
def tablero_org_gapanalisis_3():
    return render_template("pizarron/ORG/gap-analysis-3.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/gap-analisis4')
@login_required
def tablero_org_gapanalisis_4():
    return render_template("pizarron/ORG/gap-analysis-4.html")

@pizarron_org.route('/menu/inicio/pilares_il6s/ORG_menu/tablero/gap-analisis5')
@login_required
def tablero_org_gapanalisis_5():
    return render_template("pizarron/ORG/gap-analysis-5.html")