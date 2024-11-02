#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa,
sorted by ascending id.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    """Query all State objects from the database,
    ordered by id in ascending order"""
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
