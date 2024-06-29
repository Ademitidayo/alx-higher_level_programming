#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}
