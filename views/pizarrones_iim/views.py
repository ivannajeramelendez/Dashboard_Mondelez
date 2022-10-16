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

pizarron_iim = Blueprint('pizarron_iim', __name__)

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu')
@login_required
def menu_pilares_iim():
    return render_template("pilares/IIM/menu_pilares_iim.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero')
@login_required
def tablero_iim():
    return render_template("tableros/tablero_iim.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/mision')
@login_required
def tablero_iim_mission():
    return render_template("pizarron/IIM/mission.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/organigrama')
@login_required
def tablero_iim_organigrama():
    return render_template("pizarron/IIM/organigrama-pilar.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/cbn')
@login_required
def tablero_iim_cbn():
    from models.models_cbn import Cbn_iim
    dato = Cbn_iim.query.all()
    return render_template("pizarron/IIM/cbn-link.html", dato=dato)

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/cbn/<id>/edit', methods=["get", "post"])
@login_required
def tablero_iim_cbn_edit(id):
    from models.models_cbn import Cbn_iim, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Cbn_iim.query.get(id)
    if dato is None:
        abort(404)
    form = FormCbn_iim(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("pizarron_iim.tablero_iim_cbn"))
    return render_template("pizarron/IIM/cbn-link_edit.html", form=form)

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/team-capability')
@login_required
def tcapability_iim(id='1'):
    # IMPORTACION DE MODELOS
    from models.models_team_capability import Teamcapability_iim
    # DEFINE EL OBTENER ALL DATA CON GET Y ID
    paros = Teamcapability_iim.query.get(id)
    if id == '1':
        paros = Teamcapability_iim.query.all()
    else:
        # TOMA COMO FILTRO EL ID Y ALL DATA DE LA TABLA
        paros = Teamcapability_iim.query.filter_by(TeamcapabilityId=id)
    # MUESTRA EL DATA CON LA DEFINICION
    paros = Teamcapability_iim.query.all()
    return render_template("pizarron/IIM/team-capability.html", paros=paros)

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/team-capability/<id>/edit', methods=["get", "post"])
@login_required
def tcapability_edit_iim(id):
    from models.models_team_capability import Teamcapability_iim, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Teamcapability_iim.query.get(id)
    # SI NO LA ENCUENTRA
    if art is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormTeamcapability_iim(obj=art)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("pizarron_iim.tcapability_iim"))
    return render_template("pizarron/IIM/tcapability_edit.html", form=form)

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/grafica-capability')
@login_required
def tablero_iim_capability():
    return render_template("pizarron/IIM/grafica-capability.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/pilar-swot')
@login_required
def tablero_iim_plar_swot():
    return render_template("pizarron/IIM/pilar-swot.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/plan-90-dias')
@login_required
def tablero_iim_plan_90():
    return render_template("pizarron/IIM/90-dias.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/grafica-sistemas-herramienta')
@login_required
def tablero_iim_sistemas_herramienta():
    return render_template("pizarron/IIM/grafica-sistemas-herramienta.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/status-loss')
@login_required
def tablero_iim_status_loss():
    return render_template("pizarron/IIM/estatus-perdidas.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/gap-analisis2')
@login_required
def tablero_iim_gapanalisis_2():
    return render_template("pizarron/IIM/gap-analysis-2.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/gap-analisis3')
@login_required
def tablero_iim_gapanalisis_3():
    return render_template("pizarron/IIM/gap-analysis-3.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IIM_menu/tablero/gap-analisis4')
@login_required
def tablero_iim_gapanalisis_4():
    return render_template("pizarron/IMM/gap-analysis-4.html")

@pizarron_iim.route('/menu/inicio/pilares_il6s/IMM_menu/tablero/gap-analisis5')
@login_required
def tablero_iim_gapanalisis_5():
    return render_template("pizarron/IIM/gap-analysis-5.html")