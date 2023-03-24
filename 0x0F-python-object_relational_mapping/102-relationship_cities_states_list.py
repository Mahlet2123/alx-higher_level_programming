#!/usr/bin/python3
""" a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State, Base


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
    rows = session.query(State).order_by(State.id).all()
    for row in rows:
        for city in row.cities:
            print("{}: {} -> {}".format(city.id, city.name, row.name))

    session.commit()
    session.close()
