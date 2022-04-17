from datetime import datetime, timedelta
from dataclasses import dataclass, field
from models import User, Bid
from typing import List, Dict
from enum import Enum

import string
import secrets


class SessionType(str, Enum):
    Creator = "Creator"
    Winner = "Winner"
    Participant = "Participant"


@dataclass
class EmulatorUser:
    name: str
    password: str = ""
    history: Dict["EmulatorSession", SessionType] = field(default_factory=dict)

    def add(self, session: "EmulatorSession"):
        pass

    def delete(self, session: "EmulatorSession"):
        pass

    def __post_init__(self):
        if self.password == "":
            self.password = self.generate_password()

    @staticmethod
    def generate_password():
        specials = '-_@!#^'
        alphabet = string.ascii_letters + string.digits + specials

        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(20))
            if (sum(c.islower() for c in password) >= 4
                    and sum(c.isupper() for c in password) >= 4
                    and sum(c.isdigit() for c in password) >= 4
                    and sum(c in specials for c in password) >= 2):
                return password


class EmulatorCustomer(EmulatorUser):
    pass


class EmulatorProvider(EmulatorUser):
    pass


@dataclass
class EmulatorBid:
    session: "Session"
    user: "User"
    rate: float
    datetime: datetime = datetime.now()


@dataclass
class EmulatorSession:
    name: str
    customer: EmulatorCustomer
    max_value: float
    percent: float  # В процентах, а не дробях
    duration: int  # В минутах

    winner: EmulatorProvider = None
    providers: List[EmulatorProvider] = field(default_factory=list)
    bids: List[EmulatorBid] = field(default_factory=list)

    current_value: float = 0
    start_time: datetime = datetime.now()

    def __post_init__(self):
        self.current_value = self.max_value

    def __hash__(self):  # Сделать возврат идентификатора из базы. Пока просто рандомные числа
        return int(self.duration * self.percent * self.max_value + self.name.__hash__())

    def add(self, provider: EmulatorProvider):
        if provider == self.winner:
            return

        if provider not in self.providers:
            self.providers.append(provider)
            provider.add(self)

        self.bids.append(EmulatorBid(self, provider, self.current_value))

        if self.current_value - self.max_value * self.percent / 100 < 0.01:
            self.end()
            return

        self.current_value -= self.max_value * self.percent / 100
        self.winner = provider

        if self.remained.seconds / 60 < 1:
            print("Ставка за минуту до конца сделки")
            self.duration += 1

    @property
    def remained(self) -> timedelta:  # Возвращает в секундах сука
        return self.start_time + timedelta(minutes=self.duration) - datetime.now()

    def end(self):
        self.customer.history[self] = SessionType.Creator
        self.winner.history[self] = SessionType.Winner
        self.winner.delete(self)
        self.customer.delete(self)

        for provider in self.providers:
            if provider != self.winner:
                provider.history[self] = SessionType.Participant
