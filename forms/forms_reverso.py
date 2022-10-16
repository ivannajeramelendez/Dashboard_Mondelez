from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, IntegerField,\
    TextAreaField, SelectField, PasswordField, FloatField
from wtforms.fields.html5 import EmailField, DateTimeLocalField, DateField, DateTimeField
from flask_wtf.file import FileField
from wtforms.widgets import TextArea
from wtforms.validators import Required
from datetime import datetime

class FormReverso_bosch_1(FlaskForm):
    verifica_area_limpia = StringField("reverso")
    verifica_tools_limpias = StringField("reverso")
    verifica_cuchillas_de_corte = StringField("reverso")
    verifica_canal_tableta = StringField("reverso")
    verifica_cadena_tableta = StringField("reverso")
    verifica_poleas_limpias = StringField("reverso")
    verifica_discos_limpios = StringField("reverso")
    verifica_cuchillas_goma = StringField("reverso")
    verifica_poleas_estado = StringField("reverso")
    verifica_interior_libre_metal = StringField("reverso")
    verifica_discos_estado = StringField("reverso")
    verifica_mordazas_limpias = StringField("reverso")
    primera_hora = StringField("reverso")
    segunda_hora = StringField("reverso")
    tercera_hora = StringField("reverso")
    cuarta_hora = StringField("reverso")
    quinta_hora = StringField("reverso")
    sexta_hora = StringField("reverso")
    septima_hora = StringField("reverso")
    octava_hora = StringField("reverso")
    novena_hora = StringField("reverso")
    temperatura_de_mordazas = StringField("reverso")
    temperatura_de_sellado = StringField("reverso")
    limpieza_bosch = StringField("reverso")
    limpieza_emp_manual = StringField("reverso")
    ancho_de_tira = StringField("reverso")
    espesor_de_tira = StringField("reverso")
    tira_sin_grumos = StringField("reverso")
    tira_sin_manchas = StringField("reverso")
    min_paros_planeados = StringField("reverso")
    min_paros_no_planeados = StringField("reverso")
    num_paros_menores = StringField("reverso")
    ge = StringField("reverso")
    vel_banda_2_transporte = StringField("reverso")
    vel_banda_4_transporte = StringField("reverso")
    altura_de_tira_sis_relajacion = StringField("reverso")
    apertura_polea_1 = StringField("reverso")
    apertura_polea_2 = StringField("reverso")
    apertura_polea_3 = StringField("reverso")
    dosificador_de_talco = StringField("reverso")
    t_de_espera_dosificador = StringField("reverso")
    t_de_act_en_dosificador = StringField("reverso")
    corte_long_tableta = StringField("reverso")
    long_de_etiquetado = StringField("reverso")
    posicion_del_cursor = StringField("reverso")
    posicion_del_prod_bobina = StringField("reverso")
    posicion_de_impresion = StringField("reverso")
    vel_banda_6 = StringField("reverso")
    sobre_incompleto_inicio = StringField("reverso")
    sobre_incompleto_medio = StringField("reverso")
    sobre_incompleto_fin = StringField("reverso")
    mal_sellado_inicio = StringField("reverso")
    mal_sellado_medio = StringField("reverso")
    mal_sellado_fin = StringField("reverso")
    sobre_mordido_inicio = StringField("reverso")
    sobre_mordido_medio = StringField("reverso")
    sobre_mordido_fin = StringField("reverso")
    sobre_descentrado_inicio = StringField("reverso")
    sobre_descentrado_medio = StringField("reverso")
    sobre_descentrado_fin = StringField("reverso")
    sobre_con_impresion_defectuosa_inicio = StringField("reverso")
    sobre_con_impresion_defectuosa_medio = StringField("reverso")
    sobre_con_impresion_defectuosa_final = StringField("reverso")
    tableta_deforme_inicio = StringField("reverso")
    tableta_deforme_medio = StringField("reverso")
    tableta_deforme_fin = StringField("reverso")
    sobre_mal_codificado_inicio = StringField("reverso")
    sobre_mal_codificado_medio = StringField("reverso")
    sobre_mal_codificado_fin = StringField("reverso")

class FormReverso_bosch_2(FlaskForm):
    verifica_area_limpia = StringField("reverso")
    verifica_tools_limpias = StringField("reverso")
    verifica_cuchillas_de_corte = StringField("reverso")
    verifica_canal_tableta = StringField("reverso")
    verifica_cadena_tableta = StringField("reverso")
    verifica_poleas_limpias = StringField("reverso")
    verifica_discos_limpios = StringField("reverso")
    verifica_cuchillas_goma = StringField("reverso")
    verifica_poleas_estado = StringField("reverso")
    verifica_interior_libre_metal = StringField("reverso")
    verifica_discos_estado = StringField("reverso")
    verifica_mordazas_limpias = StringField("reverso")
    primera_hora = StringField("reverso")
    segunda_hora = StringField("reverso")
    tercera_hora = StringField("reverso")
    cuarta_hora = StringField("reverso")
    quinta_hora = StringField("reverso")
    sexta_hora = StringField("reverso")
    septima_hora = StringField("reverso")
    octava_hora = StringField("reverso")
    novena_hora = StringField("reverso")
    temperatura_de_mordazas = StringField("reverso")
    temperatura_de_sellado = StringField("reverso")
    limpieza_bosch = StringField("reverso")
    limpieza_emp_manual = StringField("reverso")
    ancho_de_tira = StringField("reverso")
    espesor_de_tira = StringField("reverso")
    tira_sin_grumos = StringField("reverso")
    tira_sin_manchas = StringField("reverso")
    min_paros_planeados = StringField("reverso")
    min_paros_no_planeados = StringField("reverso")
    num_paros_menores = StringField("reverso")
    ge = StringField("reverso")
    vel_banda_2_transporte = StringField("reverso")
    vel_banda_4_transporte = StringField("reverso")
    altura_de_tira_sis_relajacion = StringField("reverso")
    apertura_polea_1 = StringField("reverso")
    apertura_polea_2 = StringField("reverso")
    apertura_polea_3 = StringField("reverso")
    dosificador_de_talco = StringField("reverso")
    t_de_espera_dosificador = StringField("reverso")
    t_de_act_en_dosificador = StringField("reverso")
    corte_long_tableta = StringField("reverso")
    long_de_etiquetado = StringField("reverso")
    posicion_del_cursor = StringField("reverso")
    posicion_del_prod_bobina = StringField("reverso")
    posicion_de_impresion = StringField("reverso")
    vel_banda_6 = StringField("reverso")
    sobre_incompleto_inicio = StringField("reverso")
    sobre_incompleto_medio = StringField("reverso")
    sobre_incompleto_fin = StringField("reverso")
    mal_sellado_inicio = StringField("reverso")
    mal_sellado_medio = StringField("reverso")
    mal_sellado_fin = StringField("reverso")
    sobre_mordido_inicio = StringField("reverso")
    sobre_mordido_medio = StringField("reverso")
    sobre_mordido_fin = StringField("reverso")
    sobre_descentrado_inicio = StringField("reverso")
    sobre_descentrado_medio = StringField("reverso")
    sobre_descentrado_fin = StringField("reverso")
    sobre_con_impresion_defectuosa_inicio = StringField("reverso")
    sobre_con_impresion_defectuosa_medio = StringField("reverso")
    sobre_con_impresion_defectuosa_final = StringField("reverso")
    tableta_deforme_inicio = StringField("reverso")
    tableta_deforme_medio = StringField("reverso")
    tableta_deforme_fin = StringField("reverso")
    sobre_mal_codificado_inicio = StringField("reverso")
    sobre_mal_codificado_medio = StringField("reverso")
    sobre_mal_codificado_fin = StringField("reverso")