from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Cbn_fi(db.Model):
    """Tabla CBN Link"""
    __tablename__ = 'cbn_fi'
    id = Column(Integer, primary_key=True)
    elemento_cbn = Column(String(100), nullable=False)
    temas = Column(String(100), nullable=False)
    capacidad = Column(String(100), nullable=False)
    medidas = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))