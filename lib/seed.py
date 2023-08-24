# from faker import Faker
import time
from models import User, Habit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    session.query(Habit).delete()

    user_list = [
        {'username': 'alijohn', 'name': 'Alice Johnson'},
        {'username': 'bobsmith', 'name': 'Bob Smith'},
        {'username': 'evewill', 'name': 'Eve Williams'},
        {'username': 'johnq', 'name': 'John Quil'},
        {'username': 'olixav', 'name': 'Olivia Xavier'},
        {'username': 'nonelso', 'name': 'Noah Nelson'},
        {'username': 'sophiam', 'name': 'Sophia Miller'},
        {'username': 'lucdavi', 'name': 'Lucas Davis'},
        {'username': 'avajones', 'name': 'Ava Jones'},
        {'username': 'harpark', 'name': 'Henry Parker'}
        ]
    users = []
    for user_data in user_list:
        user = User(username=user_data['username'], name=user_data['name'])
        session.add(user)
        session.commit()

        users.append(user)

    habits = [
    Habit(title='Read a book', frequency=0, streak=2, user_id=users[0].id, last_checked_in=int(time.time())),
    Habit(title='Workout', frequency=2, streak=4, user_id=users[1].id, last_checked_in=int(time.time())),
    Habit(title='Drink water', frequency=1, streak=3, user_id=users[1].id, last_checked_in=int(time.time())),
    Habit(title='Meditate', frequency=3, streak=1, user_id=users[2].id, last_checked_in=int(time.time())),
    Habit(title='Write journal', frequency=2, streak=2, user_id=users[3].id, last_checked_in=int(time.time())),
    Habit(title='Stretch', frequency=1, streak=4, user_id=users[5].id, last_checked_in=int(time.time())),
    Habit(title='Practice coding', frequency=4, streak=3, user_id=users[5].id, last_checked_in=int(time.time())),
    Habit(title='Eat veggies', frequency=1, streak=1, user_id=users[8].id, last_checked_in=int(time.time())),
    Habit(title='Listen to music', frequency=2, streak=3, user_id=users[9].id, last_checked_in=int(time.time())),
    Habit(title='Call a friend', frequency=3, streak=2, user_id=users[4].id, last_checked_in=int(time.time()))
]

    session.bulk_save_objects(habits)
    session.commit()
    session.close()