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
from forms.forms_ctos_edit import *

app = Flask(__name__)

usuario = Blueprint('usuario', __name__, template_folder='templates', static_folder='static')

@usuario.route('/publicaciones/')
@usuario.route('/publicaciones/<id>')
@login_required
def inicio(id='0'):
    from models.models import Articulos, Categorias
    # SE LLAMA LA VARIABLE DE LA TABLA
    categoria = Categorias.query.get(id)
    if id == '0':
        articulos = Articulos.query.all()
    else:
        articulos = Articulos.query.filter_by(CategoriaId=id)
    # MUESTRA TODA LA TABLA
    categorias = Categorias.query.all()
    return render_template("publicaciones.html", articulos=articulos, categorias=categorias, categoria=categoria)

@usuario.route('/publicaciones/new', methods=["get", "post"])
@login_required
def articulos_new():
    from models.models import Articulos, Categorias, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # IMPORTA EL FORM EN CUESTION
    form = FormArticulo()
    categorias = [(c.id, c.nombre) for c in Categorias.query.all()[1:]]
    form.CategoriaId.choices = categorias
    # VALIDA EL FORM
    if form.validate_on_submit():
        try:
            f = form.photo.data
            nombre_fichero = secure_filename(f.filename)
            f.save(usuario.root_path + "/static/upload/" + nombre_fichero)
        except:
            nombre_fichero = ""
        art = Articulos()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        art.image = nombre_fichero
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("usuario.inicio"))
    else:
        return render_template("articulos_new.html", form=form)

@usuario.route('/publicaciones/<id>/edit', methods=["get", "post"])
@login_required
def articulos_edit(id):
    from models.models import Articulos, Categorias, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Articulos.query.get(id)
    # ABORTA SI NO ENCUENTRA NADA
    if art is None:
        abort(404)
    # SE IMPORTA EL FORM
    form = FormArticulo(obj=art)
    categorias = [(c.id, c.nombre) for c in Categorias.query.all()[1:]]
    form.CategoriaId.choices = categorias
    # SI VALIDA LA EL FORM PROCEDE
    if form.validate_on_submit():
        # GUARDA LOS NUEVOS DATOS
        form.populate_obj(art)
        db.session.commit()
        return redirect(url_for("usuario.inicio"))
    return render_template("articulos_new.html", form=form)

@usuario.route('/publicaciones/<id>/delete', methods=["get", "post"])
@login_required
def articulos_delete(id):
    from models.models import Articulos, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    art = Articulos.query.get(id)
    # SI NO LO ENCUENTRA ABORTA
    if art is None:
        abort(404)
    # IMPORTA EL FORM EN CUESTION
    form = FormSINO()
    # SI VALIDA EL FORM ELIMINA
    if form.validate_on_submit():
        if form.si.data:
            # MANDA LA ORDEN A ELIMINAR
            db.session.delete(art)
            db.session.commit()
        return redirect(url_for("usuario.inicio"))
    return render_template("articulos_delete.html", form=form, art=art)

@usuario.route('/pizarron/calendario')
@login_required
def calendario():
    return render_template("calendario.html")

@usuario.route('/usuarios/<id>/edit', methods=["get", "post"])
@login_required
def usuarios_edit(id):
    from models.models import Usuarios, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    user = Usuarios.query.get(id)
    # SI NO LA ENCUENTRA
    if user is None:
        abort(404)
    # IMPORTAMOS EL FORM A EDITAR
    form = FormUsuario(obj=user)
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM SE SOBREESCRIBE
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_usuarios"))
    return render_template("usuarios_edit.html", form=form)

@usuario.route('/usuarios/<id>/delete', methods=["get", "post"])
@login_required
def usuarios_delete(id):
    from models.models import Usuarios, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # SE CREA LA VARIABLE DE LA TABLA
    user = Usuarios.query.get(id)
    # SI NO LA ENCUENTRA
    if user is None:
        abort(404)
    # IMPORTAMOS EL FORM A UTILIZAR
    form = FormSINO()
    if form.validate_on_submit():
        # SI ENCUENTRA EL FORM Y LA DATA SE ELIMINA
        if form.si.data:
            db.session.delete(user)
            db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_usuarios"))
    return render_template("usuarios_delete.html", form=form, user=user)

@usuario.route('/niveles/new', methods=["get", "post"])
@login_required
def categorias_new():
    from models.models import Categorias, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    form = FormCategoria(request.form)
    if form.validate_on_submit():
        cat = Categorias(nombre=form.nombre.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_categoria"))
    else:
        return render_template("categorias_new.html", form=form)

@usuario.route('/niveles/<id>/edit', methods=["get", "post"])
@login_required
def categorias_edit(id):
    from models.models import Categorias, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Categorias.query.get(id)
    if cat is None:
        abort(404)
    form = FormCategoria(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_categoria"))
    return render_template("categorias_new.html", form=form)

@usuario.route('/niveles/<id>/delete', methods=["get", "post"])
@login_required
def categorias_delete(id):
    from models.models import Categorias, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Categorias.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_categoria"))
    return render_template("categorias_delete.html", form=form, cat=cat)

@usuario.route('/perfil/<username>', methods=["get", "post"])
@login_required
def perfil(username):
    from models.models import Usuarios, Articulos, db
    articulos = Articulos.query.all()
    user = Usuarios.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    form = FormUsuario(request.form, obj=user)
    del form.password
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("pizarron_fi.pizarron"))
    return render_template("usuarios_new.html", form=form, perfil=True, articulos=articulos)

@usuario.route('/changepassword/<username>', methods=["get", "post"])
@login_required
def changepassword(username):
    from models.models import Usuarios, db
    user = Usuarios.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    form = FormChangePassword()
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("pizarron_fi.pizarron"))
    return render_template("changepassword.html", form=form)
