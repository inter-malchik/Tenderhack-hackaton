from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


# Если нам понадобятся конкретные классы Provider и Customer, то наследуем их отсюда
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key = Column(String)


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    start_rate = Column(Integer)
    percent = Column(Integer)
    approximation = Column(Float)
    is_active = Column(Boolean)
    coeff = Column(Float)


class Bid(Base):
    __tablename__ = 'bids'

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    datetime = Column(DateTime)
    rate = Column(Integer)

    session_id_map = relationship("Session", foreign_keys=[session_id])
    user_id_map = relationship("User", foreign_keys=[user_id])



