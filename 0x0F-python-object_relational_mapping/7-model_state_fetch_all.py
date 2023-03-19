#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    for instance in session.query(State).order_by(states.id):
        print("{}: {}".format(instance.id, instance.name) 
    session.close()
