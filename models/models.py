from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Categorias(db.Model):
    """Categorías de las Publicaciones"""
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    articulos = relationship("Articulos", cascade="all, delete-orphan", backref="Categorias", lazy='dynamic')

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Lineas(db.Model):
    """Lineas """
    __tablename__ = 'lineas'
    id = Column(Integer, primary_key=True)
    linea = Column(String(100))

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Secciones(db.Model):
    """Secciones """
    __tablename__ = 'secciones'
    id = Column(Integer, primary_key=True)
    seccion = Column(String(100))

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Areas(db.Model):
    """Areas """
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True)
    area = Column(String(100))
    loss = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Articulos(db.Model):
    """Publicaciones de nuestra Dashboard"""
    __tablename__ = 'articulos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255))
    horario = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    CategoriaId = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    categoria = relationship("Categorias", backref="Articulos")

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Sku(db.Model):
    """Cto Fallas"""
    __tablename__ = 'sku'
    id = Column(Integer, primary_key=True)
    sku = Column(Integer)
    producto = Column(String(100), nullable=False)
    maquina = Column(String(100), nullable=False)
    descripcion = Column(String(100), nullable=False)
    buom_descripcion = Column(String(100), nullable=False)
    kg_min = Column(Float)
    ea_min = Column(Float)
    linea = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Auditor_comentario(db.Model):
    """Comentario Auditor"""
    __tablename__ = 'auditor_comentario_fi'
    id = Column(Integer, primary_key=True)
    comentario = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Usuarios(db.Model):
    """Usuarios"""
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password_hash = Column(String(128), nullable=False)
    nombre = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    admin = Column(Integer)
    user_fi = Column(Integer)
    leader_fi = Column(Integer)
    user_am = Column(Integer)
    user_auditor = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Flask-Login integracion
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def is_admin(self):
        return self.admin

    def is_user_auditor(self):
        return self.user_auditor

    def is_user_fi(self):
        return self.user_fi

    def is_leader_fi(self):
        return self.leader_fi
    
    def is_user_am(self):
        return self.user_am

class Empleados_cto(db.Model):
    """Empleados"""
    __tablename__ = 'empleados'
    id = Column(Integer, primary_key=True)
    NumeroEmpleadoMondelez = Column(Integer)
    NombreEmpleadoMondelez = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Turno(db.Model):
    """Turno"""
    __tablename__ = 'turno'
    id = Column(Integer, primary_key=True)
    turno = Column(String(100), nullable=False)
    valor = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Notificaciones(db.Model):
    """Turno"""
    __tablename__ = 'notificaciones'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    notificacion = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

# --------------------------------------------------------------- INICIO CTO'S  --------------------------------------------------------------#
# -------------------------------------------- SLAB 1's  --------------------------------------------#
class Cto1s_bosch_1(db.Model):
    """Formulario Cto 1s Prototipo"""
    __tablename__ = 'cto1s_bosch_1'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(100), nullable=False)
    turno = Column(Integer)
    lote = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    nombre_operador = Column(String(100), nullable=False)
    nombre_operador_cambios = Column(String(100), nullable=False)
    codigo_sobre = Column(String(100), nullable=False)
    tiempo_corrida = Column(String(100), nullable=False)
    observaciones = Column(String(100), nullable=False)
    rework = Column(Float)
    scrap = Column(Float)
    lote_bobina = Column(String(100), nullable=False)
    bobina_consumida = Column(Float)
    total_display = Column(Float)
    ge = Column(Float)
    quality_loss = Column(Float)
    speed_loss = Column(Float)
    sku = Column(String(100))
    maquina = Column(Float)
    tiempo_maximo = Column(Integer)
    tiempo_usado = Column(Integer)
    tiempo_operativo = Column(Float)
    min_paro_planeado = Column(Integer)
    # INCIO CAMPOS HIDDEN DEFAULT
    area = Column(String)
    linea_cto = Column(String)
    year = Column(Integer)
    planta = Column(String)
    seccion = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Cto1s_bosch_1_fallas(db.Model):
    """Formulario Cto 1s bosch 1 fallas"""
    __tablename__ = 'cto1s_bosch_1_fallas'
    id = Column(Integer, primary_key=True)
    falla = Column(Integer, nullable=False)
    perdida = Column(String)
    frec = Column(Integer, nullable=False)
    total = Column(Float)
    falla_2 = Column(Integer, nullable=False)
    frec_2 = Column(Integer, nullable=False)
    total_2 = Column(Float)
    falla_3 = Column(Integer, nullable=False)
    frec_3 = Column(Integer, nullable=False)
    total_3 = Column(Float)
    falla_4 = Column(Integer, nullable=False)
    frec_4 = Column(Integer, nullable=False)
    total_4 = Column(Float)
    falla_5 = Column(Integer, nullable=False)
    frec_5 = Column(Integer, nullable=False)
    total_5 = Column(Float)
    falla_6 = Column(Integer, nullable=False)
    frec_6 = Column(Integer, nullable=False)
    total_6 = Column(Float)
    falla_7 = Column(Integer, nullable=False)
    frec_7 = Column(Integer, nullable=False)
    total_7 = Column(Float)
    falla_8 = Column(Integer, nullable=False)
    frec_8 = Column(Integer, nullable=False)
    total_8 = Column(Float)
    falla_9 = Column(Integer, nullable=False)
    frec_9 = Column(Integer, nullable=False)
    total_9 = Column(Float)
    falla_10 = Column(Integer, nullable=False)
    frec_10 = Column(Integer, nullable=False)
    total_10 = Column(Float)
    falla_11 = Column(Integer, nullable=False)
    frec_11 = Column(Integer, nullable=False)
    total_11 = Column(Float)
    falla_12 = Column(Integer, nullable=False)
    frec_12 = Column(Integer, nullable=False)
    total_12 = Column(Float)
    falla_13 = Column(Integer, nullable=False)
    frec_13 = Column(Integer, nullable=False)
    total_13 = Column(Float)
    falla_14 = Column(Integer, nullable=False)
    frec_14 = Column(Integer, nullable=False)
    total_14 = Column(Float)
    falla_15 = Column(Integer, nullable=False)
    frec_15 = Column(Integer, nullable=False)
    total_15 = Column(Float)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Ctofallas(db.Model):
    """Cto Fallas"""
    __tablename__ = 'ctofallas'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    falla = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    perdida = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Cto1s_bosch_2(db.Model):
    """Formulario Cto 1s Bosch 2"""
    __tablename__ = 'cto1s_bosch_2'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(100), nullable=False)
    turno = Column(Integer)
    lote = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    nombre_operador = Column(String(100), nullable=False)
    nombre_operador_cambios = Column(String(100), nullable=False)
    codigo_sobre = Column(String(100), nullable=False)
    tiempo_corrida = Column(String(100), nullable=False)
    observaciones = Column(String(100), nullable=False)
    rework = Column(Float)
    scrap = Column(Float)
    lote_bobina = Column(String(100), nullable=False)
    bobina_consumida = Column(Float)
    total_display = Column(Float)
    ge = Column(Float)
    quality_loss = Column(Float)
    speed_loss = Column(Float)
    sku = Column(String(100))
    maquina = Column(Float)
    tiempo_maximo = Column(Integer)
    tiempo_usado = Column(Integer)
    tiempo_operativo = Column(Float)
    min_paro_planeado = Column(Integer)
    # INCIO CAMPOS HIDDEN DEFAULT
    area = Column(String)
    linea_cto = Column(String)
    year = Column(Integer)
    planta = Column(String)
    seccion = Column(String)
    # FIN CAMPOS HIDDEN DEFAULT
    falla = Column(Integer, nullable=False)
    perdida = Column(String)
    frec = Column(Integer, nullable=False)
    total = Column(Float)
    falla_2 = Column(Integer, nullable=False)
    frec_2 = Column(Integer, nullable=False)
    total_2 = Column(Float)
    falla_3 = Column(Integer, nullable=False)
    frec_3 = Column(Integer, nullable=False)
    total_3 = Column(Float)
    falla_4 = Column(Integer, nullable=False)
    frec_4 = Column(Integer, nullable=False)
    total_4 = Column(Float)
    falla_5 = Column(Integer, nullable=False)
    frec_5 = Column(Integer, nullable=False)
    total_5 = Column(Float)
    falla_6 = Column(Integer, nullable=False)
    frec_6 = Column(Integer, nullable=False)
    total_6 = Column(Float)
    falla_7 = Column(Integer, nullable=False)
    frec_7 = Column(Integer, nullable=False)
    total_7 = Column(Float)
    falla_8 = Column(Integer, nullable=False)
    frec_8 = Column(Integer, nullable=False)
    total_8 = Column(Float)
    falla_9 = Column(Integer, nullable=False)
    frec_9 = Column(Integer, nullable=False)
    total_9 = Column(Float)
    falla_10 = Column(Integer, nullable=False)
    frec_10 = Column(Integer, nullable=False)
    total_10 = Column(Float)
    falla_11 = Column(Integer, nullable=False)
    frec_11 = Column(Integer, nullable=False)
    total_11 = Column(Float)
    falla_12 = Column(Integer, nullable=False)
    frec_12 = Column(Integer, nullable=False)
    total_12 = Column(Float)
    falla_13 = Column(Integer, nullable=False)
    frec_13 = Column(Integer, nullable=False)
    total_13 = Column(Float)
    falla_14 = Column(Integer, nullable=False)
    frec_14 = Column(Integer, nullable=False)
    total_14 = Column(Float)
    falla_15 = Column(Integer, nullable=False)
    frec_15 = Column(Integer, nullable=False)
    total_15 = Column(Float)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
# -------------------------------------------- SLAB 6's  --------------------------------------------#
class Cto6s_prototipo_l1(db.Model):
    """Formulario Cto 6s Prototipo"""
    __tablename__ = 'cto6s_prototipo_l1'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(100), nullable=False)
    turno = Column(Integer)
    lote = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    nombre_operador = Column(String(100), nullable=False)
    nombre_operador_cambios = Column(String(100), nullable=False)
    codigo_sobre = Column(String(100), nullable=False)
    tiempo_corrida = Column(String(100), nullable=False)
    observaciones = Column(String(100), nullable=False)
    rework = Column(Float)
    scrap = Column(Float)
    lote_bobina = Column(String(100), nullable=False)
    bobina_consumida = Column(Float)
    total_display = Column(Float)
    ge = Column(Float)
    quality_loss = Column(Float)
    speed_loss = Column(Float)
    sku = Column(String(100))
    maquina = Column(Float)
    tiempo_maximo = Column(Integer)
    tiempo_usado = Column(Integer)
    tiempo_operativo = Column(Float)
    min_paro_planeado = Column(Integer)
    # INCIO CAMPOS HIDDEN DEFAULT
    area = Column(String)
    linea_cto = Column(String)
    year = Column(Integer)
    planta = Column(String)
    seccion = Column(String)
    # FIN CAMPOS HIDDEN DEFAULT
    falla = Column(Integer, nullable=False)
    frec = Column(Integer, nullable=False)
    total = Column(Float)
    falla_2 = Column(Integer, nullable=False)
    frec_2 = Column(Integer, nullable=False)
    total_2 = Column(Float)
    falla_3 = Column(Integer, nullable=False)
    frec_3 = Column(Integer, nullable=False)
    total_3 = Column(Float)
    falla_4 = Column(Integer, nullable=False)
    frec_4 = Column(Integer, nullable=False)
    total_4 = Column(Float)
    falla_5 = Column(Integer, nullable=False)
    frec_5 = Column(Integer, nullable=False)
    total_5 = Column(Float)
    falla_6 = Column(Integer, nullable=False)
    frec_6 = Column(Integer, nullable=False)
    total_6 = Column(Float)
    falla_7 = Column(Integer, nullable=False)
    frec_7 = Column(Integer, nullable=False)
    total_7 = Column(Float)
    falla_8 = Column(Integer, nullable=False)
    frec_8 = Column(Integer, nullable=False)
    total_8 = Column(Float)
    falla_9 = Column(Integer, nullable=False)
    frec_9 = Column(Integer, nullable=False)
    total_9 = Column(Float)
    falla_10 = Column(Integer, nullable=False)
    frec_10 = Column(Integer, nullable=False)
    total_10 = Column(Float)
    falla_11 = Column(Integer, nullable=False)
    frec_11 = Column(Integer, nullable=False)
    total_11 = Column(Float)
    falla_12 = Column(Integer, nullable=False)
    frec_12 = Column(Integer, nullable=False)
    total_12 = Column(Float)
    falla_13 = Column(Integer, nullable=False)
    frec_13 = Column(Integer, nullable=False)
    total_13 = Column(Float)
    falla_14 = Column(Integer, nullable=False)
    frec_14 = Column(Integer, nullable=False)
    total_14 = Column(Float)
    falla_15 = Column(Integer, nullable=False)
    frec_15 = Column(Integer, nullable=False)
    total_15 = Column(Float)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Cto6s_prototipo_l2(db.Model):
    """Formulario Cto 6s Prototipo"""
    __tablename__ = 'cto6s_prototipo_l2'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(100), nullable=False)
    turno = Column(Integer)
    lote = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    nombre_operador = Column(String(100), nullable=False)
    nombre_operador_cambios = Column(String(100), nullable=False)
    codigo_sobre = Column(String(100), nullable=False)
    tiempo_corrida = Column(String(100), nullable=False)
    observaciones = Column(String(100), nullable=False)
    rework = Column(Float)
    scrap = Column(Float)
    lote_bobina = Column(String(100), nullable=False)
    bobina_consumida = Column(Float)
    total_display = Column(Float)
    ge = Column(Float)
    quality_loss = Column(Float)
    speed_loss = Column(Float)
    sku = Column(String(100))
    maquina = Column(Float)
    tiempo_maximo = Column(Integer)
    tiempo_usado = Column(Integer)
    tiempo_operativo = Column(Float)
    min_paro_planeado = Column(Integer)
    # INCIO CAMPOS HIDDEN DEFAULT
    area = Column(String)
    linea_cto = Column(String)
    year = Column(Integer)
    planta = Column(String)
    seccion = Column(String)
    # FIN CAMPOS HIDDEN DEFAULT
    falla = Column(Integer, nullable=False)
    frec = Column(Integer, nullable=False)
    total = Column(Float)
    falla_2 = Column(Integer, nullable=False)
    frec_2 = Column(Integer, nullable=False)
    total_2 = Column(Float)
    falla_3 = Column(Integer, nullable=False)
    frec_3 = Column(Integer, nullable=False)
    total_3 = Column(Float)
    falla_4 = Column(Integer, nullable=False)
    frec_4 = Column(Integer, nullable=False)
    total_4 = Column(Float)
    falla_5 = Column(Integer, nullable=False)
    frec_5 = Column(Integer, nullable=False)
    total_5 = Column(Float)
    falla_6 = Column(Integer, nullable=False)
    frec_6 = Column(Integer, nullable=False)
    total_6 = Column(Float)
    falla_7 = Column(Integer, nullable=False)
    frec_7 = Column(Integer, nullable=False)
    total_7 = Column(Float)
    falla_8 = Column(Integer, nullable=False)
    frec_8 = Column(Integer, nullable=False)
    total_8 = Column(Float)
    falla_9 = Column(Integer, nullable=False)
    frec_9 = Column(Integer, nullable=False)
    total_9 = Column(Float)
    falla_10 = Column(Integer, nullable=False)
    frec_10 = Column(Integer, nullable=False)
    total_10 = Column(Float)
    falla_11 = Column(Integer, nullable=False)
    frec_11 = Column(Integer, nullable=False)
    total_11 = Column(Float)
    falla_12 = Column(Integer, nullable=False)
    frec_12 = Column(Integer, nullable=False)
    total_12 = Column(Float)
    falla_13 = Column(Integer, nullable=False)
    frec_13 = Column(Integer, nullable=False)
    total_13 = Column(Float)
    falla_14 = Column(Integer, nullable=False)
    frec_14 = Column(Integer, nullable=False)
    total_14 = Column(Float)
    falla_15 = Column(Integer, nullable=False)
    frec_15 = Column(Integer, nullable=False)
    total_15 = Column(Float)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Cto6s_prototipo_l3(db.Model):
    """Formulario Cto 6s Prototipo"""
    __tablename__ = 'cto6s_prototipo_l3'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(100), nullable=False)
    turno = Column(Integer)
    lote = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    nombre_operador = Column(String(100), nullable=False)
    nombre_operador_cambios = Column(String(100), nullable=False)
    codigo_sobre = Column(String(100), nullable=False)
    tiempo_corrida = Column(String(100), nullable=False)
    observaciones = Column(String(100), nullable=False)
    rework = Column(Float)
    scrap = Column(Float)
    lote_bobina = Column(String(100), nullable=False)
    bobina_consumida = Column(Float)
    total_display = Column(Float)
    ge = Column(Float)
    quality_loss = Column(Float)
    speed_loss = Column(Float)
    sku = Column(String(100))
    maquina = Column(Float)
    tiempo_maximo = Column(Integer)
    tiempo_usado = Column(Integer)
    tiempo_operativo = Column(Float)
    min_paro_planeado = Column(Integer)
    # INCIO CAMPOS HIDDEN DEFAULT
    area = Column(String)
    linea_cto = Column(String)
    year = Column(Integer)
    planta = Column(String)
    seccion = Column(String)
    # FIN CAMPOS HIDDEN DEFAULT
    falla = Column(Integer, nullable=False)
    frec = Column(Integer, nullable=False)
    total = Column(Float)
    falla_2 = Column(Integer, nullable=False)
    frec_2 = Column(Integer, nullable=False)
    total_2 = Column(Float)
    falla_3 = Column(Integer, nullable=False)
    frec_3 = Column(Integer, nullable=False)
    total_3 = Column(Float)
    falla_4 = Column(Integer, nullable=False)
    frec_4 = Column(Integer, nullable=False)
    total_4 = Column(Float)
    falla_5 = Column(Integer, nullable=False)
    frec_5 = Column(Integer, nullable=False)
    total_5 = Column(Float)
    falla_6 = Column(Integer, nullable=False)
    frec_6 = Column(Integer, nullable=False)
    total_6 = Column(Float)
    falla_7 = Column(Integer, nullable=False)
    frec_7 = Column(Integer, nullable=False)
    total_7 = Column(Float)
    falla_8 = Column(Integer, nullable=False)
    frec_8 = Column(Integer, nullable=False)
    total_8 = Column(Float)
    falla_9 = Column(Integer, nullable=False)
    frec_9 = Column(Integer, nullable=False)
    total_9 = Column(Float)
    falla_10 = Column(Integer, nullable=False)
    frec_10 = Column(Integer, nullable=False)
    total_10 = Column(Float)
    falla_11 = Column(Integer, nullable=False)
    frec_11 = Column(Integer, nullable=False)
    total_11 = Column(Float)
    falla_12 = Column(Integer, nullable=False)
    frec_12 = Column(Integer, nullable=False)
    total_12 = Column(Float)
    falla_13 = Column(Integer, nullable=False)
    frec_13 = Column(Integer, nullable=False)
    total_13 = Column(Float)
    falla_14 = Column(Integer, nullable=False)
    frec_14 = Column(Integer, nullable=False)
    total_14 = Column(Float)
    falla_15 = Column(Integer, nullable=False)
    frec_15 = Column(Integer, nullable=False)
    total_15 = Column(Float)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Cto6s_prototipo_l4(db.Model):
    """Formulario Cto 6s Prototipo"""
    __tablename__ = 'cto6s_prototipo_l4'
    id = Column(Integer, primary_key=True)
    fecha = Column(String(100), nullable=False)
    turno = Column(Integer)
    lote = Column(String(100), nullable=False)
    linea = Column(String(100), nullable=False)
    nombre_operador = Column(String(100), nullable=False)
    nombre_operador_cambios = Column(String(100), nullable=False)
    codigo_sobre = Column(String(100), nullable=False)
    tiempo_corrida = Column(String(100), nullable=False)
    observaciones = Column(String(100), nullable=False)
    rework = Column(Float)
    scrap = Column(Float)
    lote_bobina = Column(String(100), nullable=False)
    bobina_consumida = Column(Float)
    total_display = Column(Float)
    ge = Column(Float)
    quality_loss = Column(Float)
    speed_loss = Column(Float)
    sku = Column(String(100))
    maquina = Column(Float)
    tiempo_maximo = Column(Integer)
    tiempo_usado = Column(Integer)
    tiempo_operativo = Column(Float)
    min_paro_planeado = Column(Integer)
    # INCIO CAMPOS HIDDEN DEFAULT
    area = Column(String)
    linea_cto = Column(String)
    year = Column(Integer)
    planta = Column(String)
    seccion = Column(String)
    # FIN CAMPOS HIDDEN DEFAULT
    falla = Column(Integer, nullable=False)
    frec = Column(Integer, nullable=False)
    total = Column(Float)
    falla_2 = Column(Integer, nullable=False)
    frec_2 = Column(Integer, nullable=False)
    total_2 = Column(Float)
    falla_3 = Column(Integer, nullable=False)
    frec_3 = Column(Integer, nullable=False)
    total_3 = Column(Float)
    falla_4 = Column(Integer, nullable=False)
    frec_4 = Column(Integer, nullable=False)
    total_4 = Column(Float)
    falla_5 = Column(Integer, nullable=False)
    frec_5 = Column(Integer, nullable=False)
    total_5 = Column(Float)
    falla_6 = Column(Integer, nullable=False)
    frec_6 = Column(Integer, nullable=False)
    total_6 = Column(Float)
    falla_7 = Column(Integer, nullable=False)
    frec_7 = Column(Integer, nullable=False)
    total_7 = Column(Float)
    falla_8 = Column(Integer, nullable=False)
    frec_8 = Column(Integer, nullable=False)
    total_8 = Column(Float)
    falla_9 = Column(Integer, nullable=False)
    frec_9 = Column(Integer, nullable=False)
    total_9 = Column(Float)
    falla_10 = Column(Integer, nullable=False)
    frec_10 = Column(Integer, nullable=False)
    total_10 = Column(Float)
    falla_11 = Column(Integer, nullable=False)
    frec_11 = Column(Integer, nullable=False)
    total_11 = Column(Float)
    falla_12 = Column(Integer, nullable=False)
    frec_12 = Column(Integer, nullable=False)
    total_12 = Column(Float)
    falla_13 = Column(Integer, nullable=False)
    frec_13 = Column(Integer, nullable=False)
    total_13 = Column(Float)
    falla_14 = Column(Integer, nullable=False)
    frec_14 = Column(Integer, nullable=False)
    total_14 = Column(Float)
    falla_15 = Column(Integer, nullable=False)
    frec_15 = Column(Integer, nullable=False)
    total_15 = Column(Float)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Cto_falla_slab_6s_l1(db.Model):
    """Cto Fallas Slab 6s Linea 2 Y 4"""
    __tablename__ = 'cto_falla_slab_6s_l1'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    linea = Column(String(100), nullable=False)
    perdida = Column(String(100), nullable=False)
    falla = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
# SLAB 6'S L3 Y L4
class Cto_falla_slab_6s_l3(db.Model):
    """Cto Fallas Slab 6s Linea 3 Y 4"""
    __tablename__ = 'cto_falla_slab_6s_l3'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    linea = Column(String(100), nullable=False)
    perdida = Column(String(100), nullable=False)
    falla = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

# --------------------------------------------------------------- FIN CTO'S  -----------------------------------------------------------------#
