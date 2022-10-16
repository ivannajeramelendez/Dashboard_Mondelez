from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Pilarlossmap_fi(db.Model):
    """Tabla Pilar Loss Map"""
    __tablename__ = 'pilarlossmap_fi'
    id = Column(Integer, primary_key=True)
    tema = Column(String(100), nullable=False)
    responsable = Column(String(128), nullable=False)
    objetivo = Column(String(200), nullable=False)
    estadoactual = Column(String(200), nullable=False)
    estadofuturo = Column(String(200), nullable=False)
    planesdeaccion = Column(String(200), nullable=False)
    fecha = Column(String(200), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))