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
    
    # users = [
    #     User(username='archer', name='Sharoze'),
    #     User(username='pablo', name='Joe'),
    #     User(username='pabla', name='bravo')
    # ]
    
    user_list = [{'username': 'archer', 'name': 'sharoze'},
                 {'username': 'john', 'name': 'pal'},
                 {'username': 'joe', 'name': 'mahma'},
                 {'username': 'hol', 'name': 'asdda'}]
    users = []
    for user_data in user_list:
        user = User(username=user_data['username'], name=user_data['name'])

        # add and commit individually to get IDs back
        session.add(user)
        session.commit()

        users.append(user)




    # session.bulk_save_objects(users)
    # session.commit()

    print(users[0])
    habits = [
        Habit(title='Read a book', frequency=1, streak=0, user_id=users[0].id),
        Habit(title='Workout', frequency=1, streak=6, user_id=users[0].id),
        Habit(title='Drink water', frequency=4, streak=2, user_id=users[0].id)
    ]

    session.bulk_save_objects(habits)
    session.commit()
    session.close()