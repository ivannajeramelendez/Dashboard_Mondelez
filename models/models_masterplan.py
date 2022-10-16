from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship, backref
from aplicacion.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Masterplan_fi(db.Model):
    """Tabla Master Plan"""
    __tablename__ = 'masterplan_fi'
    id = Column(Integer, primary_key=True)
    action_plan = Column(String(100), nullable=False)
    owner = Column(String(100), nullable=False)
    levl = Column(String(100), nullable=False)
    #q1_2020 = Column(String(100), nullable=False)
    #q2_2020 = Column(String(100), nullable=False)
    #q3_2020 = Column(String(100), nullable=False)
    #q4_2020 = Column(String(100), nullable=False)
    #q1_2021 = Column(String(100), nullable=False)
    #q2_2021 = Column(String(100), nullable=False)
    #q3_2021 = Column(String(100), nullable=False)
    #q4_2021 = Column(String(100), nullable=False)
    #q1_2022 = Column(String(100), nullable=False)
    #q2_2022 = Column(String(100), nullable=False)
    #q3_2022 = Column(String(100), nullable=False)
    #q4_2022 = Column(String(100), nullable=False)
    # 2020
    ene_2020 = Column(String(100), nullable=False)
    feb_2020 = Column(String(100), nullable=False)
    mar_2020 = Column(String(100), nullable=False)
    abr_2020 = Column(String(100), nullable=False)
    may_2020 = Column(String(100), nullable=False)
    jun_2020 = Column(String(100), nullable=False)
    jul_2020 = Column(String(100), nullable=False)
    ago_2020 = Column(String(100), nullable=False)
    sep_2020 = Column(String(100), nullable=False)
    oct_2020 = Column(String(100), nullable=False)
    nov_2020 = Column(String(100), nullable=False)
    dic_2020 = Column(String(100), nullable=False)
    # 2021
    ene_2021 = Column(String(100), nullable=False)
    feb_2021 = Column(String(100), nullable=False)
    mar_2021 = Column(String(100), nullable=False)
    abr_2021 = Column(String(100), nullable=False)
    may_2021 = Column(String(100), nullable=False)
    jun_2021 = Column(String(100), nullable=False)
    jul_2021 = Column(String(100), nullable=False)
    ago_2021 = Column(String(100), nullable=False)
    sep_2021 = Column(String(100), nullable=False)
    oct_2021 = Column(String(100), nullable=False)
    nov_2021 = Column(String(100), nullable=False)
    dic_2021 = Column(String(100), nullable=False)
    # 2022
    ene_2022 = Column(String(100), nullable=False)
    feb_2022 = Column(String(100), nullable=False)
    mar_2022 = Column(String(100), nullable=False)
    abr_2022 = Column(String(100), nullable=False)
    may_2022 = Column(String(100), nullable=False)
    jun_2022 = Column(String(100), nullable=False)
    jul_2022 = Column(String(100), nullable=False)
    ago_2022 = Column(String(100), nullable=False)
    sep_2022 = Column(String(100), nullable=False)
    oct_2022 = Column(String(100), nullable=False)
    nov_2022 = Column(String(100), nullable=False)
    dic_2022 = Column(String(100), nullable=False)

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))