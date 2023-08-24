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
    Habit(title='Read a book', frequency=3, streak=2, user_id=users[0].id),
    Habit(title='Workout', frequency=2, streak=4, user_id=users[1].id),
    Habit(title='Drink water', frequency=1, streak=3, user_id=users[1].id),
    Habit(title='Meditate', frequency=3, streak=1, user_id=users[2].id),
    Habit(title='Write journal', frequency=2, streak=2, user_id=users[3].id),
    Habit(title='Stretch', frequency=1, streak=4, user_id=users[5].id),
    Habit(title='Practice coding', frequency=4, streak=3, user_id=users[5].id),
    Habit(title='Eat veggies', frequency=1, streak=1, user_id=users[8].id),
    Habit(title='Listen to music', frequency=2, streak=3, user_id=users[9].id),
    Habit(title='Call a friend', frequency=3, streak=2, user_id=users[4].id)
]

    session.bulk_save_objects(habits)
    session.commit()
    session.close()