#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    argument = sys.argv[4]

    instance = (
        session.query(State).filter(State.name == (argument,)).
        order_by(State.id).all()
    )
    if instance:
        print("{}".format(instance[0].id))
    else:
        print("Not found")
    session.close()
