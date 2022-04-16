from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key = Column(String)

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    startDate = Column(DateTime)
    endDate = Column(DateTime)
    start_rate = Column(Integer)
    percent = Column(Integer)
    approximation = Column(Float)
    is_active = Column(Boolean)
    koeff = Column(Float)

class Bid(Base):
    __tablename__ = 'bids'
    session_id = Column(Integer, ForeignKey('session.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    datetime = Column(DateTime)
    rate = Column(Integer)

    session_id_map = relationship("Session", foreign_keys=[session_id])
    user_id_map = relationship("User", foreign_keys=[user_id])

