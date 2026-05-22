from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

# Association table for many-to-many relationship between users and activities
signup_table = Table(
    'signups', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('activity_id', Integer, ForeignKey('activities.id'), primary_key=True),
    Column('created_at', DateTime, default=datetime.datetime.utcnow)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role', back_populates='users')
    signups = relationship('Activity', secondary=signup_table, back_populates='participants')

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    users = relationship('User', back_populates='role')

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    schedule = Column(String)
    max_participants = Column(Integer)
    participants = relationship('User', secondary=signup_table, back_populates='signups')
