from flask import Flask, render_template, redirect, url_for, request, abort,\
    session, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from aplicacion import config
    # FORMS
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
    # VIEWS
from views.menus.views import menus
from views.dashboard.views import dashboard
from views.usuario.views import usuario
from views.ctos_consulta.views import ctos_consulta
from views.ctos.views import ctos
from views.pizarrones_lead.views import pizarron_lead
from views.pizarrones_org.views import pizarron_org
from views.pizarrones_fi.views import pizarron_fi
from views.pizarrones_am.views import pizarron_am
from views.pizarrones_pm.views import pizarron_pm
from views.pizarrones_qm.views import pizarron_qm
from views.pizarrones_iim.views import pizarron_iim
from views.pizarrones_wpi.views import pizarron_wpi
from views.pizarrones_eyt.views import pizarron_eyt
from views.pizarrones_hse.views import pizarron_hse
from views.pizarrones_sn.views import pizarron_sn
    # DRIVER
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required,\
    current_user
import os
    # APP
app = Flask(__name__)
    # VIEWS
app.register_blueprint(menus)
app.register_blueprint(dashboard)
app.register_blueprint(usuario)
app.register_blueprint(ctos_consulta)
app.register_blueprint(ctos)
app.register_blueprint(pizarron_lead)
app.register_blueprint(pizarron_org)
app.register_blueprint(pizarron_fi)
app.register_blueprint(pizarron_am)
app.register_blueprint(pizarron_pm)
app.register_blueprint(pizarron_qm)
app.register_blueprint(pizarron_iim)
app.register_blueprint(pizarron_wpi)
app.register_blueprint(pizarron_eyt)
app.register_blueprint(pizarron_hse)
app.register_blueprint(pizarron_sn)
    # SYSTEM
app.config.from_object(config)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

### ------------------------------------------------------- INICIO  PAGES ----------------------------------------------------------####
@app.route('/login', methods=['get', 'post'])
def login():
    from models.models import Usuarios
    # Control de permisos - cambiar pizarron para redirigir
    if current_user.is_authenticated:
        return redirect(url_for("menus.menu_inicio"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            return redirect(next or url_for('menus.menu_inicio'))
        form.username.errors.append("Usuario o contraseña incorrectas.")
    return render_template('inicio/login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/registro", methods=["get", "post"])
def registro():
    from models.models import Usuarios
    # Control de permisos
    if current_user.is_authenticated:
        return redirect(url_for("menus.inicio"))
    form = FormUsuario()
    if form.validate_on_submit():
        existe_usuario = Usuarios.query.\
            filter_by(username=form.username.data).first()
        if existe_usuario is None:
            user = Usuarios()
            form.populate_obj(user)
            user.admin = False
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("menus.menu_inicio"))
        form.username.errors.append("Nombre de usuario ya existe.")
    return render_template("inicio/registro.html", form=form)
### ------------------------------------------------------- FIN INICIO PAGES --------------------------------------------------------####

### ------------------------------------------------------- INICIO METAS -------------------------------------------------------------####
@app.route('/menu/inicio/metas_2021/ge&cu')
@login_required
def menu_inicio_metas_ge():
    return render_template("metas/metas_ge.html")
### ------------------------------------------------------- FIN METAS ----------------------------------------------------------------####

### ------------------------------------------------------- INICIO CTO PAGES ---------------------------------------------------------####
@app.route('/cto/vista_fallas/new', methods=["get", "post"])
@login_required
def cto_vistas_new():
    from models.models import Ctofallas
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    form = FormCtofallas(request.form)
    if form.validate_on_submit():
        cat = Ctofallas(numero=form.numero.data, falla=form.falla.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_cto"))
    else:
        return render_template("cto/cto_vistas_new.html", form=form)

@app.route('/cto/vista_fallas/<id>/edit', methods=["get", "post"])
@login_required
def cto_vistas_edit(id):
    from models.models import Ctofallas
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Ctofallas.query.get(id)
    if dato is None:
        abort(404)
    form = FormCtofallas(request.form, obj=dato)
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_cto"))
    return render_template("cto/cto_vistas_edit.html", form=form)

@app.route('/cto/vista_fallas/<id>/delete', methods=["get", "post"])
@login_required
def cto_vistas_delete(id):
    from models.models import Ctofallas
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Ctofallas.query.get(id)
    if dato is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(dato)
            db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_cto"))
    return render_template("cto/cto_vistas_delete.html", form=form, dato=dato)
### -------------------------------------------------------- FIN CTO PAGES ----------------------------------------------------------####

### -------------------------------------------------------- DIAGRAMA DE FLUJO ------------------------------------------------------####
@app.route('/diagrama')
def diagrama_de_flujo_presentacion():
    return render_template("Diagrama_de_flujo/diagrama_de_flujo.html")
### -------------------------------------------------------- FIN DIAGRAMA DE FLUJO --------------------------------------------------####

@login_manager.user_loader
def load_user(user_id):
    from models.models import Usuarios
    return Usuarios.query.get(int(user_id))

@app.errorhandler(404)
@login_required
def page_not_found(error):
    return render_template("usuario/error.html", error="Página no encontrada..."), 404
