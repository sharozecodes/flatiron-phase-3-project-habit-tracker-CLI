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
    Habit(title='Read a book', frequency=12, streak=0, user_id=users[0].id, last_checked_in = 0),
    Habit(title='Workout', frequency=24, streak=0, user_id=users[1].id, last_checked_in = 0),
    Habit(title='Drink water', frequency=3, streak=0, user_id=users[1].id, last_checked_in = 0),
    Habit(title='Meditate', frequency=3, streak=0, user_id=users[2].id, last_checked_in = 0),
    Habit(title='Write journal', frequency=12, streak=0, user_id=users[3].id, last_checked_in = 0),
    Habit(title='Stretch', frequency=2, streak=0, user_id=users[5].id, last_checked_in = 0),
    Habit(title='Practice coding', frequency=12, streak=0, user_id=users[5].id, last_checked_in = 0),
    Habit(title='Eat veggies', frequency=6, streak=0, user_id=users[8].id, last_checked_in = 0),
    Habit(title='Listen to music', frequency=24, streak=0, user_id=users[9].id, last_checked_in = 0),
    Habit(title='Call a friend', frequency=24, streak=0, user_id=users[4].id, last_checked_in = 0)
]

    session.bulk_save_objects(habits)
    session.commit()
    session.close()