from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'username={self.username}, ' + \
            f'name={self.name})'

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    frequency = Column(Integer)
    streak = Column(Integer)

    def __repr__(self):
        return f'Habit(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'frequency={self.frequency}, ' + \
            f'streak={self.streak})'