#!/usr/bin/python3
"""
a script that changes the name of a State
object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                        argv[2],
                                                        argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    stateUpdated = session.query(State).filter(State.id == 2).first()

    if stateUpdated:
        stateUpdated.name = 'New Mexico'
        session.commit()
