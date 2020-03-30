#!/usr/bin/python3
"""
Task 100:
100-relationship_states_cities.py
Create the state California and add the city San Francisco

Uses:
100-relationship_states_cities.sql
relationship_state.py
relationship_city.py
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sql_user, sql_pass, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    inst_state = State(name="California")

    inst_city = City(name="San Francsico")

    inst_state.cities = [inst_city]
    session.add(inst_state)

    session.commit()
    session.close()
