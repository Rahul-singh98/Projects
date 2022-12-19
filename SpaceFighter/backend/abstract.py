from abc import ABC, abstractmethod


class BaseWeapon(ABC):
    _power: int = 0

    def __init__(self, power: int = 10):
        self._power = power

    def getPower(self) -> int:
        return self._power


class BaseShip(ABC):
    _weapon: BaseWeapon = None

    def __init__(self, weapon: BaseWeapon):
        self._weapon = weapon

    @abstractmethod
    def on_fire(self):
        pass

    def setWeapon(self, weapon: BaseWeapon):
        self._weapon = weapon


class BaseAsteroid(ABC):
    _health: int = 10
    _x: int = 0
    _y: int = 0

    def __init__(self, x, y, health):
        self._x = x
        self._y = y
        self._health = health
