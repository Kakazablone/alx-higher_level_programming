#!/usr/bin/python3
"""Creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    host = "localhost"
    port = "3306"
    mysql_url = f"mysql+mysqldb://{username}:{password}@{host}:\
        {port}/{database}"
    engine = create_engine(mysql_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    with Session() as session:
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print(f"{city.id}: {city.name} -> {city.state.name}")
