#!/usr/bin/python3
"""
Defines the City class to represent cities in the database hbtn_0e_14_usa.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base  # Import Base from model_state to inherit from it


class City(Base):
    """City class that maps to the cities table in the database"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
