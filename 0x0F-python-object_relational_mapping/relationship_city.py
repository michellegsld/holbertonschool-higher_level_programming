#!/usr/bin/python3
"""
Task 15:
relationship_city.py
Improve the model_city.py file

Uses:
relationship_state.py
"""
from sys import argv
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    A new SQL table
    """
    __tablename__ = "cities"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("states.id"), nullable=False)
