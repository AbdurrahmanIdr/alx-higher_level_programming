#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                      sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
