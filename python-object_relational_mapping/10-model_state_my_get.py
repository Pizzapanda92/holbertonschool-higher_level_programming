#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa. If not found, displays "Not found".
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    name_to_search = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(name=name_to_search).first()

    if states:
        print('{}'.format(states.id))
    else:
        print('Not found')
    session.close()
