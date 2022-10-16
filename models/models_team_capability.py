from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

# ------------------------------------------------------------ INICIO TEAM CAPABILITY ------------------------------------------------------#
class Teamcapability_fi(db.Model):
    """Tabla Team Capability"""
    __tablename__ = 'teamcapability_fi'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    objetivo = Column(Float, default=100)
    acreditacion = Column(Float, default=0)
    calificacion = Column(Float, default=0)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))

class Team_capability_fi(db.Model):
    """Tabla Team Capability"""
    __tablename__ = 'team_capability_fi'
    id = Column(Integer, primary_key=True)
    basic_1 = Column(Integer)
    basic_2 = Column(Integer)
    basic_3 = Column(Integer)
    basic_4 = Column(Integer)
    basic_5 = Column(Integer)
    intelligence_1 = Column(Integer)
    intelligence_2 = Column(Integer)
    intelligence_3 = Column(Integer)
    intelligence_4 = Column(Integer)
    intelligence_5 = Column(Integer)
    eradication_1 = Column(Integer)
    eradication_2 = Column(Integer)
    eradication_3 = Column(Integer)
    eradication_4 = Column(Integer)
    eradication_5 = Column(Integer)
    eradication_6 = Column(Integer)
    eradication_7 = Column(Integer)
    prevention_1 = Column(Integer)
    prevention_2 = Column(Integer)
    prevention_3 = Column(Integer)
    prevention_4 = Column(Integer)
    prevention_5 = Column(Integer)
    # Seccion del leader
    basic_1_leader = Column(Integer)
    basic_2_leader = Column(Integer)
    basic_3_leader = Column(Integer)
    basic_4_leader = Column(Integer)
    basic_5_leader = Column(Integer)
    intelligence_1_leader = Column(Integer)
    intelligence_2_leader = Column(Integer)
    intelligence_3_leader = Column(Integer)
    intelligence_4_leader = Column(Integer)
    intelligence_5_leader = Column(Integer)
    eradication_1_leader = Column(Integer)
    eradication_2_leader = Column(Integer)
    eradication_3_leader = Column(Integer)
    eradication_4_leader = Column(Integer)
    eradication_5_leader = Column(Integer)
    eradication_6_leader = Column(Integer)
    eradication_7_leader = Column(Integer)
    prevention_1_leader = Column(Integer)
    prevention_2_leader = Column(Integer)
    prevention_3_leader = Column(Integer)
    prevention_4_leader = Column(Integer)
    prevention_5_leader = Column(Integer)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))