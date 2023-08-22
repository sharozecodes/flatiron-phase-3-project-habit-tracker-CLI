from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'username={self.title}, ' + \
            f'name={self.platform})'

