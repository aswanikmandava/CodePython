from dataclasses import dataclass

@dataclass
class ETA:
    user: str
    driver: str
    seconds: int

@dataclass
class User:
    name: str

class Driver(User):
    pass

class Passenger(User):
    pass