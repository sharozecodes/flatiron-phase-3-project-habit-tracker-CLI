from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Habit  

engine = create_engine("sqlite:///db/habittracker.db")
Session = sessionmaker(bind=engine)
session = Session()

def new_user(username, name):
    new_user_instance = User(username=username, name=name)
    session.add(new_user_instance)
    session.commit()
    return new_user_instance

def check_username(username):
    return session.query(User).filter_by(username=username).first() == None    

def find_by_username(username):
    return session.query(User).filter_by(username=username).first()

def add_habit(title, frequency, user_id):
    new_habit = Habit(title=title, frequency=frequency, streak=0, user_id=user_id)
    session.add(new_habit)
    session.commit()
    print("Habit added successfully!")

def find_by_habit(text, user_id):
    query = session.query(Habit).filter_by(user_id=user_id).filter(Habit.title.ilike(f"%{text}%"))
    return query.all()

def view_all_habit(user_id):
    return session.query(Habit).filter_by(user_id=user_id).all()

def edit_habit(habit_id, title, frequency):
    query = session.query(Habit).filter_by(id=habit_id).first()
    query.title = title
    query.frequency = frequency
    session.commit()

def delete_habit(habit_id):
    query = session.query(Habit).filter_by(id=habit_id).first()
    session.delete(query)
    session.commit()