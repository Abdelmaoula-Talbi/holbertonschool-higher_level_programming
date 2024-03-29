#!/usr/bin/python3
"""
A module that representes a script that lists all State
objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
