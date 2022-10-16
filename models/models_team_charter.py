from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Teamcharter_fi(db.Model):
    """Tabla Team Charter"""
    __tablename__ = 'teamcharter_fi'
    id = Column(Integer, primary_key=True)
    propositos = Column(String(100), nullable=False)
    resultados = Column(String(100), nullable=False)
    estrategia = Column(String(100), nullable=False)
    principios = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Teamcharter_comite_fi(db.Model):
    """Tabla Team Charter"""
    __tablename__ = 'teamcharter_fi_comite'
    id = Column(Integer, primary_key=True)
    miembro = Column(String(100), nullable=False)
    area = Column(String(100), nullable=False)
    rol = Column(String(100), nullable=False)
    sistema = Column(String(100), nullable=False)
    firma = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))