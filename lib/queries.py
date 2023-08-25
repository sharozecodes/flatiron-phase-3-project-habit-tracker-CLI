from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Habit  
import time
from cli import logo

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

def reset_habit(habit_id):
    query = session.query(Habit).filter_by(id=habit_id).first()
    query.streak = 0
    session.commit()

def check_in(habit_id):
    time_now = int(time.time())
    query = session.query(Habit).filter_by(id=habit_id).first()
    hours_passed = (time_now - query.last_checked_in) / 3600
    if(hours_passed > query.frequency):
        print("\noops the streak broke :(\nLet's try again")
        query.streak = 0
        session.commit()
    else:
        query.streak += 1
        session.commit()

def print_name(user_id):
    query = session.query(User).filter_by(id=user_id).first()
    time.sleep(3)
    logo()
    print(f"\nHello, {query.name}!\n")
    time.sleep(3)