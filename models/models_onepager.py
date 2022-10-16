from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Onepager_fi(db.Model):
    """Tabla Onepager"""
    __tablename__ = 'onepager_fi'
    id = Column(Integer, primary_key=True)
    propositos_pilar = Column(String(100), nullable=False)
    resultados_esperados = Column(String(100), nullable=False)
    metrics = Column(String(100), nullable=False)
    baseline = Column(String(100), nullable=False)
    last_year = Column(String(100), nullable=False)
    target_year = Column(String(100), nullable=False)
    actual_result = Column(String(100), nullable=False)
    improvement_base = Column(String(100), nullable=False)
    jipm_criteria = Column(String(100), nullable=False)
    standar_work = Column(String(100), nullable=False)
    system_owner = Column(String(100), nullable=False)
    swp_documented = Column(String(100), nullable=False)
    health_check = Column(String(100), nullable=False)
    system_tracks = Column(String(100), nullable=False)
    system_range = Column(String(100), nullable=False)
    assessment_date = Column(String(100), nullable=False)
    pilar_leader = Column(String(100), nullable=False)
    training_status = Column(String(100), nullable=False)
    qualification_date = Column(String(100), nullable=False)
    qualified_by = Column(String(100), nullable=False)
    assessment_score = Column(String(100), nullable=False)
    ready_to_approve = Column(String(100), nullable=False)
    tpm_coach = Column(String(100), nullable=False)
    gaps = Column(String)
    addressed_by = Column(String)
    estimated_completion_date = Column(String)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))