#!/usr/bin/python3
""" This module defines a Class City """
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ Class City that inherits from Base and
        links to a table named cities """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    """Establish a many-to-one relationship with State"""
    state = relationship("State", back_populates="cities")
