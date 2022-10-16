from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Scorecard_fi(db.Model):
    """Tabla Scorecard"""
    __tablename__ = 'scorecard_fi'
    id = Column(Integer, primary_key=True)
    categoria = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    formula = Column(String(100), nullable=False)
    criterio_de_exito = Column(String(100), nullable=False)
    unidades_medida = Column(String(100), nullable=False)
    tg = Column(String(100), nullable=False)
    fye = Column(String(100), nullable=False)
    ene = Column(String(100), nullable=False)
    feb = Column(String(100), nullable=False)
    mar = Column(String(100), nullable=False)
    abr = Column(String(100), nullable=False)
    may = Column(String(100), nullable=False)
    jun = Column(String(100), nullable=False)
    jul = Column(String(100), nullable=False)
    ago = Column(String(100), nullable=False)
    sep = Column(String(100), nullable=False)
    oct = Column(String(100), nullable=False)
    nov = Column(String(100), nullable=False)
    dic = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))