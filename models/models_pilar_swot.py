from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Pilar_swot_fi(db.Model):
    """Tabla Pilar Swot Fi"""
    __tablename__ = 'pilar_swot_fi'
    id = Column(Integer, primary_key=True)
    workprocess = Column(String)
    dueño = Column(String)
    back_up = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))