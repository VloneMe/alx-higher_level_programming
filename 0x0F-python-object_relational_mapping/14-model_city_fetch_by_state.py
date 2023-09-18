#!/usr/bin/python3
"""
This script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == "__main__":
    """
    Database oprational
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    filter = State.id == City.state_id

    for q in (session.query(State.name, City.id, City.name).filter(filter)):
        print(q[0] + ": (" + str(q[1]) + ") " + q[2])
