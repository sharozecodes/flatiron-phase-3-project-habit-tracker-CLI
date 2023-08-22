from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Habit  

def new_user(username, name):
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user_instance = User(username=username, name=name)
    session.add(new_user_instance)
    session.commit()
    print("User added successfully!")

def find_by_username(username):
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(User).filter_by(username=username).first()

def add_habit(title, frequency, user_id):
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    new_habit = Habit(title=title, frequency=frequency, streak=0, user_id=user_id)
    session.add(new_habit)
    session.commit()
    print("Habit added successfully!")

