#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
and prints the new state's id after creation.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Creat new state
    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    print('{}'.format(new_state.id))

    session.close()
