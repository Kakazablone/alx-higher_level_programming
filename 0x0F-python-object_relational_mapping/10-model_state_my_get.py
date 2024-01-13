#!/usr/bin/python3
"""Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    username, password, database, state = argv[1], argv[2], argv[3], argv[4]
    host = "localhost"
    port = "3306"
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_name = session.query(State).filter_by(name=state).first()
        if state_name:
            print(f"{state_name.id}")
        else:
            print("Not found")
