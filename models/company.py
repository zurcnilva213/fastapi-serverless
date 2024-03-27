from .base_model import Model
from sqlalchemy import Integer, String, DateTime, Enum, Column, Time, Boolean, func, JSON, ForeignKey, Text, Date
from sqlalchemy.orm import relationship


class Company(Model):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=True)
    name = Column(String(255), nullable=True)
    type = Column(Enum('facebook', 'web', 'yelp'))
    free_service = Column(String(255), nullable=True)
    service_type = Column(String(255), nullable=True)
    service_area = Column(Text, nullable=True)
    type_of_offer = Column(String(255), nullable=True)
    about_us = Column(Text, nullable=True)   # what company does
    phone = Column(String(100), nullable=True)
    decline_service = Column(String(255), nullable=True)   # EST, PST, MST
    time_zone = Column(String(100), nullable=True)   # EST, PST, MST
    operation_start = Column(Time, nullable=True)
    operation_end = Column(Time, nullable=True)
    working_days = Column(JSON, nullable=True)  # update to json
    after_hours = Column(Boolean)
    after_hours_only = Column(Boolean)
    zip_codes = Column(JSON, nullable=True)  # update to json
    active = Column(Boolean)
    auto_reply = Column(Boolean)
    same_day_appointment = Column(Boolean)
    notes = Column(Text, nullable=True)
    podium_id = Column(Integer, ForeignKey('podium.id'), nullable=True)  # Define foreign key column
    podium = relationship("Podium", backref="company_mappings")
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())



