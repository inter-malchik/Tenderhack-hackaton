from models import Base, User, Session, Bid
from sqlalchemy import create_engine
import sqlalchemy.orm as sorm
from emulation import EmulatorBid, EmulatorSession, EmulatorProvider, EmulatorCustomer, EmulatorUser
from typing import Dict


CONNECTION_STRING = "postgresql://postgres:qwerty123@localhost:5432/session"


def session_demonstration(engine):
    user = User(name="Anton", key="1234")
    sess = Session(name="Name")

    with sorm.Session(engine) as session:
        session.add_all([user, sess])
        session.flush()

        bid = Bid(session_id=sess.id, user_id=user.id, rate=10)
        session.add_all([bid])
        session.commit()


def test():
    Ivan = EmulatorCustomer("Ivan")
    Alex = EmulatorCustomer("Alex")
    Leo = EmulatorCustomer("Leo")

    IS = EmulatorSession("IS", Ivan, 1000, 2.5, 3)
    print(IS.name, IS.customer, IS.current_value)

    for chelick in (Alex, Leo, Alex):
        IS.add(chelick)
        print(chelick.name, "added:", IS.name, IS.current_value)

    #  sleep(IS.remained.total_seconds())  # Спим до конца сессии

    IS.end()
    print("End", IS.current_value, IS.winner)
    print("Alex", Alex.history.get(IS))
    print("Leo", Leo.history.get(IS))


if __name__ == '__main__':
    engine = create_engine(CONNECTION_STRING)
    Base.metadata.create_all(engine)  # Создает таблицы, если они ещё не созданы

    Ivan = EmulatorCustomer("Ivan")
    Artyom = EmulatorCustomer("Artyom")
    Maria = EmulatorCustomer("Maria")

    IS = EmulatorSession("IS", Ivan, 1000, 2.5, 3)
    VT = EmulatorSession("VT", Artyom, 2000, 1, 3)
    CT = EmulatorSession("CT", Maria, 500, 5, 3)

    Alex = EmulatorCustomer("Alex")
    Leo = EmulatorCustomer("Leo")
    Mila = EmulatorCustomer("Mila")
    Anton = EmulatorCustomer("Anton")
    Ksenia = EmulatorCustomer("Ksenia")

    tokens: Dict[str, EmulatorUser] = {
        Ivan.password: Ivan,
        Artyom.password: Artyom,
        Maria.password: Maria,
        Alex.password: Alex,
        Leo.password: Leo,
        Mila.password: Mila,
        Anton.password: Anton,
        Ksenia.password: Ksenia,
    }

    test()
