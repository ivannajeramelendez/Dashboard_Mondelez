from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Gapanalisis_fi_1(db.Model):
    """Tabla GAP Analisis 1"""
    __tablename__ = 'gapanalisis_fi_1'
    id = Column(Integer, primary_key=True)
    objetivo_analisis = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    causa_raices = Column(String(100), nullable=False)
    plan_accion = Column(String(100), nullable=False)
    responsable = Column(String(100), nullable=False)
    fecha_1 = Column(String(100), nullable=False)
    explique = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_1_efecto(db.Model):
    """Tabla GAP Analisis 1 Efecto"""
    __tablename__ = 'gapanalisis_fi_1_efecto'
    id = Column(Integer, primary_key=True)
    efecto_1 = Column(String)
    efecto_2 = Column(String)
    efecto_3 = Column(String)
    efecto_4 = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_2(db.Model):
    """Tabla GAP Analisis 2"""
    __tablename__ = 'gapanalisis_fi_2'
    id = Column(Integer, primary_key=True)
    objetivo_analisis = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    causa_raices = Column(String(100), nullable=False)
    plan_accion = Column(String(100), nullable=False)
    responsable = Column(String(100), nullable=False)
    fecha_1 = Column(String(100), nullable=False)
    explique = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_2_efecto(db.Model):
    """Tabla GAP Analisis 2 Efecto"""
    __tablename__ = 'gapanalisis_fi_2_efecto'
    id = Column(Integer, primary_key=True)
    efecto_1 = Column(String)
    efecto_2 = Column(String)
    efecto_3 = Column(String)
    efecto_4 = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_3(db.Model):
    """Tabla GAP Analisis 3"""
    __tablename__ = 'gapanalisis_fi_3'
    id = Column(Integer, primary_key=True)
    objetivo_analisis = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    causa_raices = Column(String(100), nullable=False)
    plan_accion = Column(String(100), nullable=False)
    responsable = Column(String(100), nullable=False)
    fecha_1 = Column(String(100), nullable=False)
    explique = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_3_efecto(db.Model):
    """Tabla GAP Analisis 3 Efecto"""
    __tablename__ = 'gapanalisis_fi_3_efecto'
    id = Column(Integer, primary_key=True)
    efecto_1 = Column(String)
    efecto_2 = Column(String)
    efecto_3 = Column(String)
    efecto_4 = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_4(db.Model):
    """Tabla GAP Analisis 4"""
    __tablename__ = 'gapanalisis_fi_4'
    id = Column(Integer, primary_key=True)
    objetivo_analisis = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    causa_raices = Column(String(100), nullable=False)
    plan_accion = Column(String(100), nullable=False)
    responsable = Column(String(100), nullable=False)
    fecha_1 = Column(String(100), nullable=False)
    explique = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_4_efecto(db.Model):
    """Tabla GAP Analisis 4 Efecto"""
    __tablename__ = 'gapanalisis_fi_4_efecto'
    id = Column(Integer, primary_key=True)
    efecto_1 = Column(String)
    efecto_2 = Column(String)
    efecto_3 = Column(String)
    efecto_4 = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_5(db.Model):
    """Tabla GAP Analisis 5"""
    __tablename__ = 'gapanalisis_fi_5'
    id = Column(Integer, primary_key=True)
    objetivo_analisis = Column(String(100), nullable=False)
    fecha = Column(String(100), nullable=False)
    causa_raices = Column(String(100), nullable=False)
    plan_accion = Column(String(100), nullable=False)
    responsable = Column(String(100), nullable=False)
    fecha_1 = Column(String(100), nullable=False)
    explique = Column(String(100), nullable=False)
    status = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Gapanalisis_fi_5_efecto(db.Model):
    """Tabla GAP Analisis 5 Efecto"""
    __tablename__ = 'gapanalisis_fi_5_efecto'
    id = Column(Integer, primary_key=True)
    efecto_1 = Column(String)
    efecto_2 = Column(String)
    efecto_3 = Column(String)
    efecto_4 = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))