#!/usr/bin/python3
"""Defines a Class State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """Class State that inherits from Base and
        links to a table named state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    """Establish a one-to-many relationship with City"""
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
