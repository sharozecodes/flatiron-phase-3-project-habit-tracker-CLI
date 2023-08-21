from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User  

def new_user(username, name):
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user_instance = User(username=username, name=name)
    session.add(new_user_instance)
    session.commit()
    print("User added successfully!")
