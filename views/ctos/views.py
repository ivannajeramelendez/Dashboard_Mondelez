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
from forms.forms_reverso import *

app = Flask(__name__)

ctos = Blueprint('ctos', __name__, template_folder='templates', static_folder='static')

# INICIO SLAB 1'S ===============================================================
@ctos.route('/menu/inicio/ctos/Slab1s/bosch_1', methods=["get", "post"])
@login_required
def cto_proto_2():
    from models.models import Cto1s_bosch_1, Cto1s_bosch_1_fallas, Ctofallas, Sku, Turno, Empleados_cto, db
    from models.models_reverso import Reverso_bosch_1, db
    # Form
    form = FormCto1s_bosch_1()
    fallas = FormCto1s_bosch_1_fallas()
    reverso = FormReverso_bosch_1()
    # Query
    empleado = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    empleado_cambio = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    categorias = [(c.numero, c.falla) for c in Ctofallas.query.all()[0:]]
    sku = [(c.kg_min, c.producto) for c in Sku.query.all()[0:2]]
    fallas.falla.choices = categorias
    fallas.falla_2.choices = categorias
    fallas.falla_3.choices = categorias
    fallas.falla_4.choices = categorias
    fallas.falla_5.choices = categorias
    fallas.falla_6.choices = categorias
    fallas.falla_7.choices = categorias
    fallas.falla_8.choices = categorias
    fallas.falla_9.choices = categorias
    fallas.falla_10.choices = categorias
    fallas.falla_11.choices = categorias
    fallas.falla_12.choices = categorias
    fallas.falla_13.choices = categorias
    fallas.falla_14.choices = categorias
    fallas.falla_15.choices = categorias
    form.sku.choices = sku
    form.nombre_operador.choices = empleado
    form.nombre_operador_cambios.choices = empleado_cambio
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cto1s_bosch_1()
        reverse = Reverso_bosch_1()
        ark = Cto1s_bosch_1_fallas()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        fallas.populate_obj(ark)
        reverso.populate_obj(reverse)
        db.session.add(art)
        db.session.add(ark)
        db.session.add(reverse)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_success_ctos"))
    else:
        return render_template("Slab_1s/cto_slab_1s_bosch_1.html", form=form, reverso=reverso, fallas=fallas)

@ctos.route('/menu/inicio/ctos/Slab1s/bosch_2', methods=["get", "post"])
@login_required
def cto_slab_1s_bosch_2():
    from models.models import Cto1s_bosch_2, Ctofallas, Sku, Empleados_cto, db
    from models.models_reverso import Reverso_bosch_2, db
    # IMPORTA EL FORM EN CUESTION
    form = FormCto1s_bosch_2()
    reverso = FormReverso_bosch_2()
    # COLOCA LA BUSQUEDA EN SQL DEL ELEMENTO
    empleado = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    empleado_cambio = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    categorias = [(c.numero, c.falla) for c in Ctofallas.query.all()[0:]]
    sku = [(c.kg_min, c.producto) for c in Sku.query.all()[2:4]]
    form.falla.choices = categorias
    form.falla_2.choices = categorias
    form.falla_3.choices = categorias
    form.falla_4.choices = categorias
    form.falla_5.choices = categorias
    form.falla_6.choices = categorias
    form.falla_7.choices = categorias
    form.falla_8.choices = categorias
    form.falla_9.choices = categorias
    form.falla_10.choices = categorias
    form.falla_11.choices = categorias
    form.falla_12.choices = categorias
    form.falla_13.choices = categorias
    form.falla_14.choices = categorias
    form.falla_15.choices = categorias
    form.sku.choices = sku
    form.nombre_operador.choices = empleado
    form.nombre_operador_cambios.choices = empleado_cambio
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cto1s_bosch_2()
        reverse = Reverso_bosch_2()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        reverso.populate_obj(reverse)
        db.session.add(art)
        db.session.add(reverse)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_success_ctos"))
    else:
        return render_template("Slab_1s/cto_slab_1s_bosch_2.html", form=form, reverso=reverso)

# INICIO SLAB 6'S ===============================================================
@ctos.route('/menu/inicio/ctos/Slab6s/L1/prototype', methods=["get", "post"])
@login_required
def cto_slab_6s_prototipo_l1():
    from models.models import Cto6s_prototipo_l1, Cto_falla_slab_6s_l1, Sku, Empleados_cto, db
    # IMPORTA EL FORM EN CUESTION
    form = FormCto6s_prototipo_l1()
    formu = FormSku()
    # COLOCA LA BUSQUEDA EN SQL DEL ELEMENTO
    empleado = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    empleado_cambio = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    categorias = [(c.numero, c.falla) for c in Cto_falla_slab_6s_l1.query.all()[0:]]
    sku = [(c.kg_min, c.producto) for c in Sku.query.all()[4:11]]
    form.falla.choices = categorias
    form.falla_2.choices = categorias
    form.falla_3.choices = categorias
    form.falla_4.choices = categorias
    form.falla_5.choices = categorias
    form.falla_6.choices = categorias
    form.falla_7.choices = categorias
    form.falla_8.choices = categorias
    form.falla_9.choices = categorias
    form.falla_10.choices = categorias
    form.falla_11.choices = categorias
    form.falla_12.choices = categorias
    form.falla_13.choices = categorias
    form.falla_14.choices = categorias
    form.falla_15.choices = categorias
    form.sku.choices = sku
    form.nombre_operador.choices = empleado
    form.nombre_operador_cambios.choices = empleado_cambio
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cto6s_prototipo_l1()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_success_ctos"))
    else:
        return render_template("Slab_6s/cto_slab_6s_prototipo_l1.html", form=form)

@ctos.route('/menu/inicio/ctos/Slab6s/L2/prototype', methods=["get", "post"])
@login_required
def cto_slab_6s_prototipo_l2():
    from models.models import Cto6s_prototipo_l2, Cto_falla_slab_6s_l1, Sku, Empleados_cto, db
    # IMPORTA EL FORM EN CUESTION
    form = FormCto6s_prototipo_l2()
    formu = FormSku()
    # COLOCA LA BUSQUEDA EN SQL DEL ELEMENTO
    empleado = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    empleado_cambio = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    categorias = [(c.numero, c.falla) for c in Cto_falla_slab_6s_l1.query.all()[0:]]
    sku = [(c.kg_min, c.producto) for c in Sku.query.all()[4:11]]
    form.falla.choices = categorias
    form.falla_2.choices = categorias
    form.falla_3.choices = categorias
    form.falla_4.choices = categorias
    form.falla_5.choices = categorias
    form.falla_6.choices = categorias
    form.falla_7.choices = categorias
    form.falla_8.choices = categorias
    form.falla_9.choices = categorias
    form.falla_10.choices = categorias
    form.falla_11.choices = categorias
    form.falla_12.choices = categorias
    form.falla_13.choices = categorias
    form.falla_14.choices = categorias
    form.falla_15.choices = categorias
    form.sku.choices = sku
    form.nombre_operador.choices = empleado
    form.nombre_operador_cambios.choices = empleado_cambio
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cto6s_prototipo_l2()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_success_ctos"))
    else:
        return render_template("Slab_6s/cto_slab_6s_prototipo_l2.html", form=form)

@ctos.route('/menu/inicio/ctos/Slab6s/L3/prototype', methods=["get", "post"])
@login_required
def cto_slab_6s_prototipo_l3():
    from models.models import Cto6s_prototipo_l3, Cto_falla_slab_6s_l3, Sku, Empleados_cto, db
    # IMPORTA EL FORM EN CUESTION
    form = FormCto6s_prototipo_l3()
    formu = FormSku()
    # COLOCA LA BUSQUEDA EN SQL DEL ELEMENTO
    empleado = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    empleado_cambio = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    categorias = [(c.numero, c.falla) for c in Cto_falla_slab_6s_l3.query.all()[0:]]
    sku = [(c.kg_min, c.producto) for c in Sku.query.all()[11:18]]
    form.falla.choices = categorias
    form.falla_2.choices = categorias
    form.falla_3.choices = categorias
    form.falla_4.choices = categorias
    form.falla_5.choices = categorias
    form.falla_6.choices = categorias
    form.falla_7.choices = categorias
    form.falla_8.choices = categorias
    form.falla_9.choices = categorias
    form.falla_10.choices = categorias
    form.falla_11.choices = categorias
    form.falla_12.choices = categorias
    form.falla_13.choices = categorias
    form.falla_14.choices = categorias
    form.falla_15.choices = categorias
    form.sku.choices = sku
    form.nombre_operador.choices = empleado
    form.nombre_operador_cambios.choices = empleado_cambio
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cto6s_prototipo_l3()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_success_ctos"))
    else:
        return render_template("Slab_6s/cto_slab_6s_prototipo_l3.html", form=form)

@ctos.route('/menu/inicio/ctos/Slab6s/L4/prototype', methods=["get", "post"])
@login_required
def cto_slab_6s_prototipo_l4():
    from models.models import Cto6s_prototipo_l4, Cto_falla_slab_6s_l3, Sku, Empleados_cto, db
    # IMPORTA EL FORM EN CUESTION
    form = FormCto6s_prototipo_l4()
    formu = FormSku()
    # COLOCA LA BUSQUEDA EN SQL DEL ELEMENTO
    empleado = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    empleado_cambio = [(c.NumeroEmpleadoMondelez, c.NombreEmpleadoMondelez) for c in Empleados_cto.query.all()[0:]]
    categorias = [(c.numero, c.falla) for c in Cto_falla_slab_6s_l3.query.all()[0:]]
    sku = [(c.kg_min, c.producto) for c in Sku.query.all()[11:18]]
    form.falla.choices = categorias
    form.falla_2.choices = categorias
    form.falla_3.choices = categorias
    form.falla_4.choices = categorias
    form.falla_5.choices = categorias
    form.falla_6.choices = categorias
    form.falla_7.choices = categorias
    form.falla_8.choices = categorias
    form.falla_9.choices = categorias
    form.falla_10.choices = categorias
    form.falla_11.choices = categorias
    form.falla_12.choices = categorias
    form.falla_13.choices = categorias
    form.falla_14.choices = categorias
    form.falla_15.choices = categorias
    form.sku.choices = sku
    form.nombre_operador.choices = empleado
    form.nombre_operador_cambios.choices = empleado_cambio
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Cto6s_prototipo_l4()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_success_ctos"))
    else:
        return render_template("Slab_6s/cto_slab_6s_prototipo_l4.html", form=form)