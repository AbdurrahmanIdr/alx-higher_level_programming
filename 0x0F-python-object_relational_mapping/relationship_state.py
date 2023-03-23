#!/usr/bin/python3
"""
python script that contains the class
definition of a State and an instance
Base = declarative_base:
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from relationship_city import City

Base = declarative_base()


class State(Base):
    """
    class state for the state table
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(length=128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
