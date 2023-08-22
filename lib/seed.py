# from faker import Faker
import random
from models import User, Habit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Habit).delete()
    
    users = [
        User(username='pable', name='John'),
        User(username='pablo', name='Joe'),
        User(username='pabla', name='bravo')
    ]

    session.bulk_save_objects(users)
    session.commit()

    habits = [
        Habit(title='adadaf'),
        Habit(title='asfafa'),
        Habit(title='sdvcscdsf')
    ]

    session.bulk_save_objects(habits)
    session.commit()
    session.close()