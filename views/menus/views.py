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

menus = Blueprint('menus', __name__, template_folder='templates', static_folder='static', static_url_path='/static/Pilares/')

@menus.route('/')
@menus.route('/menu/inicio')
@login_required
def menu_inicio():
    return render_template("inicio.html")

@menus.route('/menu/inicio/envio/ctos/')
@login_required
def menu_inicio_success_ctos():
    return render_template("success.html")

##  =========================================== MENU CTO'S ================================  ##
@menus.route('/menu/inicio/ctos')
@login_required
def menu_inicio_ctos():
    return render_template("Ctos/Entradas/ctos.html")
## ======================================= ENTRADAS
@menus.route('/menu/inicio/ctos/capturas')
@login_required
def menu_inicio_ctos_capturas():
    return render_template("Ctos/Entradas/ctos_capturas.html")

@menus.route('/menu/inicio/ctos/consulta_capturas')
@menus.route('/menu/inicio/ctos/consulta_capturas/<id>')
@login_required
def menu_inicio_ctos_consulta_capturas(id='0'):
    from models.models import Cto1s_bosch_1, Cto6s_prototipo_l1, Cto6s_prototipo_l2,\
        Cto6s_prototipo_l3, Cto6s_prototipo_l4, Cto1s_bosch_2, db
    # SE LLAMA LA VARIABLE DE LA TABLA
    if id == '0':
        registro = Cto1s_bosch_1.query.all()
        registro_dos = Cto6s_prototipo_l1.query.all()
        registro_tres = Cto6s_prototipo_l2.query.all()
        registro_cuatro = Cto6s_prototipo_l3.query.all()
        registro_cinco = Cto6s_prototipo_l4.query.all()
        registro_seis = Cto1s_bosch_2.query.all()
    else:
        registro = Cto1s_bosch_1.query.filter_by(RegistroId=id)
        registro_dos = Cto6s_prototipo_l1.query.filter_by(RegistroId=id)
        registro_tres = Cto6s_prototipo_l2.query.filter_by(RegistroId=id)
        registro_cuatro = Cto6s_prototipo_l3.query.filter_by(RegistroId=id)
        registro_cinco = Cto6s_prototipo_l4.query.filter_by(RegistroId=id)
        registro_seis = Cto1s_bosch_2.query.filter_by(RegistroId=id)
    return render_template("Ctos/Entradas/ctos_consulta_capturas.html", registro=registro, registro_dos=registro_dos, registro_tres=registro_tres,
                            registro_cuatro=registro_cuatro, registro_cinco=registro_cinco, registro_seis=registro_seis)

@menus.route('/menu/inicio/ctos/ctos_extracto_excel')
@menus.route('/menu/inicio/ctos/ctos_extracto_excel/<id>')
@login_required
def menu_inicio_ctos_extracto_excel(id='0'):
    from models.models import Cto1s_bosch_1, Cto6s_prototipo_l1, Cto6s_prototipo_l2,\
        Cto6s_prototipo_l3, Cto6s_prototipo_l4, Cto1s_bosch_2, db
    # SE LLAMA LA VARIABLE DE LA TABLA
    if id == '0':
        registro = Cto1s_bosch_1.query.all()
        registro_dos = Cto6s_prototipo_l1.query.all()
        registro_tres = Cto6s_prototipo_l2.query.all()
        registro_cuatro = Cto6s_prototipo_l3.query.all()
        registro_cinco = Cto6s_prototipo_l4.query.all()
        registro_seis = Cto1s_bosch_2.query.all()
    else:
        registro = Cto1s_bosch_1.query.filter_by(RegistroId=id)
        registro_dos = Cto6s_prototipo_l1.query.filter_by(RegistroId=id)
        registro_tres = Cto6s_prototipo_l2.query.filter_by(RegistroId=id)
        registro_cuatro = Cto6s_prototipo_l3.query.filter_by(RegistroId=id)
        registro_cinco = Cto6s_prototipo_l4.query.filter_by(RegistroId=id)
        registro_seis = Cto1s_bosch_2.query.filter_by(RegistroId=id)
    return render_template("Ctos/Entradas/ctos_extracto_excel.html", registro=registro, registro_dos=registro_dos,
                            registro_tres=registro_tres, registro_cuatro=registro_cuatro, registro_cinco=registro_cinco, registro_seis=registro_seis)
## ======================================= WATERFALL
@menus.route('/menu/inicio/ctos/ctos_extracto_gwf')
@menus.route('/menu/inicio/ctos/ctos_extracto_gwf/<id>')
@login_required
def menu_inicio_ctos_extracto_gwf(id='0'):
    from models.models import Cto1s_bosch_1, Cto6s_prototipo_l1, Cto6s_prototipo_l2,\
        Cto6s_prototipo_l3, Cto6s_prototipo_l4, Cto1s_bosch_2, db
    # SE LLAMA LA VARIABLE DE LA TABLA
    if id == '0':
        registro = Cto1s_bosch_1.query.all()
        registro_dos = Cto6s_prototipo_l1.query.all()
        registro_tres = Cto6s_prototipo_l2.query.all()
        registro_cuatro = Cto6s_prototipo_l3.query.all()
        registro_cinco = Cto6s_prototipo_l4.query.all()
        registro_seis = Cto1s_bosch_2.query.all()
    else:
        registro = Cto1s_bosch_1.query.filter_by(RegistroId=id)
        registro_dos = Cto6s_prototipo_l1.query.filter_by(RegistroId=id)
        registro_tres = Cto6s_prototipo_l2.query.filter_by(RegistroId=id)
        registro_cuatro = Cto6s_prototipo_l3.query.filter_by(RegistroId=id)
        registro_cinco = Cto6s_prototipo_l4.query.filter_by(RegistroId=id)
        registro_seis = Cto1s_bosch_2.query.filter_by(RegistroId=id)
    return render_template("Ctos/Waterfall/ctos_extracto_gwf.html", registro=registro, registro_dos=registro_dos, registro_tres=registro_tres,
                            registro_cuatro=registro_cuatro, registro_cinco=registro_cinco, registro_seis=registro_seis)
## ======================================= ADMINISTRACION
@menus.route('/menu/inicio/ctos/operadores')
@login_required
def menu_inicio_ctos_operadores():
    from models.models import Empleados_cto
    empleados = Empleados_cto.query.all()[1:]
    return render_template("Ctos/Administracion/ctos_operadores.html", empleados=empleados)

@menus.route('/menu/inicio/ctos/operadores/<id>/edit', methods=["get", "post"])
@login_required
def menu_inicio_ctos_operadores_edit(id):
    from models.models import Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    # Consulta al cto
    id = id
    slab_cto = Empleados_cto.query.get(id)
    # Formulario para editar
    cat = Empleados_cto.query.get(id)
    if cat is None:
        abort(404)
    form = FormEmpleados_cto(request.form, obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_operadores"))
    return render_template("Ctos/Administracion/ctos_operadores_edit.html", form=form, slab_cto=slab_cto)

@menus.route('/menu/inicio/ctos/operadores/<id>/delete', methods=["get", "post"])
@login_required
def menu_inicio_ctos_operadores_delete(id):
    from models.models import Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    cat = Empleados_cto.query.get(id)
    if cat is None:
        abort(404)
    form = FormSINO()
    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_operadores"))
    return render_template("categorias_delete.html", form=form, cat=cat)

@menus.route('/menu/inicio/ctos/operadores/new', methods=["get", "post"])
@login_required
def menu_inicio_ctos_operadores_new():
    from models.models import Empleados_cto, db
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    form = FormEmpleados_cto()
    # VALIDA EL FORM
    if form.validate_on_submit():
        art = Empleados_cto()
        # GRABA LA INFORMACION EN LA DATABASE
        form.populate_obj(art)
        db.session.add(art)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_operadores"))
    else:
        return render_template("Ctos/Administracion/ctos_operadores_edit.html", form=form)

@menus.route('/menu/inicio/ctos/productos')
@login_required
def menu_inicio_ctos_productos():
    from models.models import Sku
    sku = Sku.query.all()
    return render_template("Ctos/Administracion/ctos_productos.html", sku=sku)

@menus.route('/menu/inicio/ctos/modos_de_fallo')
@login_required
def menu_inicio_ctos_modos_de_fallo():
    from models.models import Ctofallas, Cto_falla_slab_6s_l1 
    cto = Ctofallas.query.all()[1:]
    cto2 = Cto_falla_slab_6s_l1.query.all()[1:]
    return render_template("Ctos/Administracion/ctos_modos_de_fallos.html", cto=cto, cto2=cto2)

@menus.route('/menu/inicio/ctos/security')
@login_required
def menu_inicio_ctos_security():
    from models.models import Sku, Cto1s_bosch_1, Categorias, Lineas, Usuarios
    sku = Sku.query.all()
    cto = Cto1s_bosch_1.query.all()
    categoria = Categorias.query.all()
    lineas = Lineas.query.all()
    user = Usuarios.query.all()
    return render_template("Ctos/Administracion/ctos_security.html", sku=sku, cto=cto, categoria=categoria, lineas=lineas, user=user)

@menus.route('/menu/inicio/ctos/Jerarquia_de_Planta')
@login_required
def menu_inicio_ctos_jerarquia_de_planta():
    from models.models import Lineas, Areas, Secciones
    lineas = Lineas.query.all()[1:]
    areas = Areas.query.all()[1:]
    secciones = Secciones.query.all()[1:]
    return render_template("Ctos/Administracion/ctos_jerarquia.html", lineas=lineas, areas=areas, secciones=secciones)

##  =========================================== DASHBOARD ============================  ##
@menus.route('/menu/inicio/ctos/dashboard/reporte_del_turno')
@login_required
def menu_inicio_dashboard_reporte_del_turno(id='1'):
    from models.models import Cto6s_prototipo_l1, Cto1s_bosch_2, Cto6s_prototipo_l2, Cto6s_prototipo_l3, Cto6s_prototipo_l4,\
        Cto1s_bosch_1, Cto1s_bosch_1_fallas,  Ctofallas, Sku, Lineas, Areas
    # OPERACIONES
        # Ge consulta de resultados
    lista_ge_1s = ((c.ge)for c in Cto1s_bosch_1.query.all())
    suma_ge_1s = [lista for lista in lista_ge_1s]
    lista_ge_1s_bosch_2 = ((c.ge)for c in Cto1s_bosch_2.query.all())
    suma_ge_1s_bosch_2 = [lista for lista in lista_ge_1s_bosch_2]
    lista_ge = ((c.ge)for c in Cto6s_prototipo_l1.query.all())
    suma_ge = [lista for lista in lista_ge]
    lista_l2 = ((c.ge)for c in Cto6s_prototipo_l2.query.all())
    suma_l2 = [lista for lista in lista_l2]
    lista_l3 = ((c.ge)for c in Cto6s_prototipo_l3.query.all())
    suma_l3 = [lista for lista in lista_l3]
    lista_l4 = ((c.ge)for c in Cto6s_prototipo_l4.query.all())
    suma_l4 = [lista for lista in lista_l4]
        # Operacion con los resultados
    largo_ge = len(suma_ge + suma_l2 + suma_l3 + suma_l4 + suma_ge_1s + suma_ge_1s_bosch_2)
    total_ge = sum(suma_ge + suma_l2 + suma_l3 + suma_l4 + suma_ge_1s + suma_ge_1s_bosch_2)
    cambio_ge =  (total_ge / largo_ge ) / 100 * 100
    resul_ge = ("{:.2f}".format(cambio_ge))
    planned = 100 - cambio_ge
    no_planned = 100 - cambio_ge
        # Frecuencia fallas
    lista_frec_1s = ((c.frec)for c in Cto1s_bosch_1_fallas.query.all())
    suma_frec_1s = [lista for lista in lista_frec_1s]
    lista_frec_1s_bosch_2 = ((c.frec)for c in Cto1s_bosch_2.query.all())
    suma_frec_1s_bosch_2 = [lista for lista in lista_frec_1s_bosch_2]
    lista_frec = ((c.frec)for c in Cto6s_prototipo_l1.query.all())
    suma_frec = [lista for lista in lista_frec]
    lista_frec_l2 = ((c.frec)for c in Cto6s_prototipo_l2.query.all())
    suma_frec_l2 = [lista for lista in lista_frec_l2]
    lista_frec_l3 = ((c.frec)for c in Cto6s_prototipo_l3.query.all())
    suma_frec_l3 = [lista for lista in lista_frec_l3]
    lista_frec_l4 = ((c.frec)for c in Cto6s_prototipo_l4.query.all())
    suma_frec_l4 = [lista for lista in lista_frec_l4]
    total_frec = sum(suma_frec + suma_frec_l2 + suma_frec_l3 + suma_frec_l4 + suma_frec_1s + suma_frec_1s_bosch_2)
    # Consultas
    lineas = Lineas.query.all()[1:]
    fallas = Cto6s_prototipo_l1.query.all()[0:]
    areas = Areas.query.all()[1:]
    # Tablas
    paros = Cto6s_prototipo_l1.query.all()
    linea_2 = Cto6s_prototipo_l2.query.all()
    linea_3 = Cto6s_prototipo_l3.query.all()
    linea_4 = Cto6s_prototipo_l4.query.all()
    slab_1s = Cto1s_bosch_1.query.all()
    bosch_2 = Cto1s_bosch_2.query.all()
    return render_template("Ctos/Dashboard/ctos_reporte_del_turno.html", fallas=fallas, lineas=lineas, areas=areas, resul_ge=resul_ge, 
    no_planned=no_planned, paros=paros, planned=planned, total_frec=total_frec, linea_2=linea_2, linea_3=linea_3, linea_4=linea_4, 
    slab_1s=slab_1s, bosch_2=bosch_2)

@menus.route('/menu/inicio/ctos/dashboard/ge')
@login_required
def menu_inicio_dashboard_ge(id='1'):
    from models.models import Cto6s_prototipo_l1, Cto1s_bosch_2, Cto6s_prototipo_l2, Cto6s_prototipo_l3, Cto6s_prototipo_l4,\
        Cto1s_bosch_1, Cto1s_bosch_1_fallas, Ctofallas, Sku, Lineas, Areas
    # OPERACIONES
        # Ge consulta de resultados
    lista_ge_1s = ((c.ge)for c in Cto1s_bosch_1.query.all())
    suma_ge_1s = [lista for lista in lista_ge_1s]
    lista_ge_1s_bosch_2 = ((c.ge)for c in Cto1s_bosch_2.query.all())
    suma_ge_1s_bosch_2 = [lista for lista in lista_ge_1s_bosch_2]
    lista_ge = ((c.ge)for c in Cto6s_prototipo_l1.query.all())
    suma_ge = [lista for lista in lista_ge]
    lista_l2 = ((c.ge)for c in Cto6s_prototipo_l2.query.all())
    suma_l2 = [lista for lista in lista_l2]
    lista_l3 = ((c.ge)for c in Cto6s_prototipo_l3.query.all())
    suma_l3 = [lista for lista in lista_l3]
    lista_l4 = ((c.ge)for c in Cto6s_prototipo_l4.query.all())
    suma_l4 = [lista for lista in lista_l4]
        # Operacion con los resultados
    largo_ge = len(suma_ge + suma_l2 + suma_l3 + suma_l4 + suma_ge_1s + suma_ge_1s_bosch_2)
    total_ge = sum(suma_ge + suma_l2 + suma_l3 + suma_l4 + suma_ge_1s + suma_ge_1s_bosch_2)
    cambio_ge =  (total_ge / largo_ge ) / 100 * 100
    resul_ge = ("{:.2f}".format(cambio_ge))
    planned = 100 - cambio_ge
    no_planned = 100 - cambio_ge
        # Frecuencia fallas
    lista_frec_1s = ((c.frec)for c in Cto1s_bosch_1_fallas.query.all())
    suma_frec_1s = [lista for lista in lista_frec_1s]
    lista_frec_1s_bosch_2 = ((c.frec)for c in Cto1s_bosch_2.query.all())
    suma_frec_1s_bosch_2 = [lista for lista in lista_frec_1s_bosch_2]
    lista_frec = ((c.frec)for c in Cto6s_prototipo_l1.query.all())
    suma_frec = [lista for lista in lista_frec]
    lista_frec_l2 = ((c.frec)for c in Cto6s_prototipo_l2.query.all())
    suma_frec_l2 = [lista for lista in lista_frec_l2]
    lista_frec_l3 = ((c.frec)for c in Cto6s_prototipo_l3.query.all())
    suma_frec_l3 = [lista for lista in lista_frec_l3]
    lista_frec_l4 = ((c.frec)for c in Cto6s_prototipo_l4.query.all())
    suma_frec_l4 = [lista for lista in lista_frec_l4]
    total_frec = sum(suma_frec + suma_frec_l2 + suma_frec_l3 + suma_frec_l4 + suma_frec_1s + suma_frec_1s_bosch_2)
    # Consultas
    lineas = Lineas.query.all()[1:]
    fallas = Cto6s_prototipo_l1.query.all()[0:]
    areas = Areas.query.all()[1:]
    # Tablas
    paros = Cto6s_prototipo_l1.query.all()
    linea_2 = Cto6s_prototipo_l2.query.all()
    linea_3 = Cto6s_prototipo_l3.query.all()
    linea_4 = Cto6s_prototipo_l4.query.all()
    slab_1s = Cto1s_bosch_1.query.all()
    bosch_2 = Cto1s_bosch_2.query.all()
    return render_template("Ctos/Dashboard/ctos_ge.html", fallas=fallas, lineas=lineas, areas=areas, resul_ge=resul_ge, 
    no_planned=no_planned, paros=paros, planned=planned, total_frec=total_frec, linea_2=linea_2, linea_3=linea_3, linea_4=linea_4, 
    slab_1s=slab_1s, bosch_2=bosch_2)

##  =========================================== ESTANDARES ============================  ##
@menus.route('/menu/inicio/estandares')
@login_required
def menu_inicio_estandares():
    return render_template("Estandares/estandares.html")

@menus.route('/menu/inicio/estandares_1')
@login_required
def menu_inicio_estandares_1():
    return render_template("Estandares/estandares_1.html")

@menus.route('/menu/inicio/estandares_2')
@login_required
def menu_inicio_estandares_2():
    return render_template("Estandares/estandares_2.html")

##  =========================================== METAS 2021 ============================  ##
@menus.route('/menu/inicio/metas_2021')
@login_required
def menu_inicio_metas_2021():
    return render_template("Metas/metas_2021.html")

##  =========================================== PIZARRON PILARES =======================  ##
@menus.route('/menu/inicio/pilares_il6s')
@login_required
def menu_inicio_pilares_il6s():
    return render_template("Pilares/pilares_il6s.html")

## ============================================= PAGES ==================================== ##
@menus.route('/menu/inicio/sku', methods=["get", "post"])
@login_required
def menu_inicio_sku():
    from models.models import Sku, Lineas, db
    # Filtro Select
    categorias = [(c.linea) for c in Lineas.query.all()[0:]]
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    form = FormSku(request.form)
    # Colocamos el form donde se direge el select
    form.linea.choices = categorias
    if form.validate_on_submit():
        cat = Sku(sku=form.sku.data, producto=form.producto.data, maquina=form.maquina.data, descripcion=form.descripcion.data,
                    kg_min=form.kg_min.data, ea_min=form.ea_min.data, buom_descripcion=form.buom_descripcion.data, linea=form.linea.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("menus.menu_inicio_ctos_operadores"))
    else:
        return render_template("cto/sku/sku.html", form=form)

@menus.route('/menu/inicio/sku/<id>/edit', methods=["get", "post"])
@login_required
def menu_inicio_sku_edit(id):
    from models.models import Sku, Lineas, db
    # Filtro Select
    categorias = [(c.linea) for c in Lineas.query.all()[0:]]
    # Control de permisos
    if not current_user.is_admin():
        abort(404)
    dato = Sku.query.get(id)
    if dato is None:
        abort(404)
    form = FormSku(request.form, obj=dato)
    form.linea.choices = categorias
    if form.validate_on_submit():
        form.populate_obj(dato)
        db.session.commit()
        return redirect(url_for("dashboard.dashboard_inicio_sku"))
    return render_template("cto/sku/sku_edit.html", form=form)
