#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    connection = engine.connect()
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    results = session.query(State).all()

    count = 1
    for states in results:
        if states.name == sys.argv[4]:
            print(states.id)
            count = 0
            break
    if count:
        print("Not found")
