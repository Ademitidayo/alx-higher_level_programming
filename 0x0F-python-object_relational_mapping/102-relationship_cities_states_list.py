#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City, State

def list_cities_states(engine):
    """Fetches and prints all City objects with associated State names."""
    Session = sessionmaker(bind=engine)
    try:
        with Session() as session:
            cities = session.query(City).order_by(City.id).all()
            for city in cities:
                print(f"{city.id}: {city.name} -> {city.state.name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    Base.metadata.create_all(engine)  # Ensures all tables are created

    list_cities_states(engine)
