# from faker import Faker
import random
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("sqlite:///db/habittracker.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(User).delete()
    
    users = [
        User(username='pable'),
        User(username='pablo'),
        User(username='pabla')
    ]

    session.bulk_save_objects(users)
    session.commit()