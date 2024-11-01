#!/usr/bin/python3
"""
Defines a SQLAlchemy class `State` mapped to the MySQL table `states`,
with columns for `id` (an auto-incremented primary key) and `name` 
(a non-nullable string up to 128 characters).
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Class definition for the State table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
