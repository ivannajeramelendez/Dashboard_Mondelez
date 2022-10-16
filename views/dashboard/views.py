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

dashboard = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static', static_url_path='/static/')

@dashboard.route("/dashboard/inicio")
@login_required
def dashboard_inicio():
    from models.models import Notificaciones
    if not current_user.is_admin():
        abort(404)
    noti = Notificaciones.query.all()
        # Numero de noti
    lista = ((c.numero)for c in Notificaciones.query.all())
    suma = [lista for lista in lista]
    largo = len(suma)
    from models.models import Sku, Cto1s_prototipo, Categorias, Lineas, Usuarios, Areas, Cto6s_prototipo_l1
    # CONSULTAS
    sku = Sku.query.all()
    cto = Cto1s_prototipo.query.all()
    categoria = Categorias.query.all()
    lineas = Lineas.query.all()
    user = Usuarios.query.all()
    # OPERACIONES TARJETAS HEADER
        # Lineas
    lista_lineas = ((c.id) for c in Lineas.query.all()[1:])
    suma_lineas = [lista for lista in lista_lineas]
    total_lineas = suma_lineas
        # Sku
    lista_sku = ((c.id) for c in Sku.query.all())
    suma_sku = [lista for lista in lista_sku]
    total_sku = suma_sku
        # User
    lista_user = ((c.id) for c in Usuarios.query.all())
    suma_user = [lista for lista in lista_user]
    total_user = suma_user
        # Cto
    lista_cto = ((c.id) for c in Cto1s_prototipo.query.all())
    suma_cto = [lista for lista in lista_cto]
    total_cto = suma_cto
    # RESULTADOS TARJETAS HEADER
    lineas_totales = (total_lineas)
    sku_totales =  (total_sku)
    usuarios_totales = (total_user)
    cto_totales = (total_cto)
    # OPERACIONES PARA LAS GRAFICAS
        # Slab 1s  
    lista_ge = ((c.ge)for c in Cto1s_prototipo.query.all())
    suma_ge = [lista for lista in lista_ge]
    largo_ge = len(suma_ge)
    total_ge = sum(suma_ge)
    cambio_ge =  (total_ge / largo_ge ) / 100 * 100
    # CALL CONSULTAS
        # Slab 1s
    resul_ge = ("{:.2f}".format(cambio_ge))
    no_planned_graph = 100 - cambio_ge
    area_loss_graph = 100 - cambio_ge
    linea_loss_graph = 100 - cambio_ge

    lineas_graph = Lineas.query.all()[1:]
    fallas_graph = Cto1s_prototipo.query.all()[0:]
    areas_graph = Areas.query.all()[1:]
    
    #ge =  ("{:.2f}".format(tiempo_usado / total_turno * 100 ))
    return render_template("Inicio/dashboard.html", sku=sku, cto=cto, lineas=lineas, user=user, 
    lineas_totales=lineas_totales, sku_totales=sku_totales, usuarios_totales=usuarios_totales, cto_totales=cto_totales,
    no_planned_graph=no_planned_graph, lineas_graph=lineas_graph, fallas_graph=fallas_graph, areas_graph=areas_graph,
    resul_ge=resul_ge, area_loss_graph=area_loss_graph, linea_loss_graph=linea_loss_graph,
    noti=noti, largo=largo)
