#!/usr/bin/python3
"""
Task 15:
relationship_state.py
Improve the model_state.py file

Uses:
100-relationship_states_cities.sql
"""
from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    A new SQL table
    """
    __tablename__ = "states"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship('City', backref='state')
