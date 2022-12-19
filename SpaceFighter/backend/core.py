from .abstract import BaseShip, BaseWeapon, BaseAsteroid


class Missile(BaseWeapon):

    def __init__(self):
        super().__init__(5)


class BattleShip(BaseShip):

    def __init__(self, weapon: BaseWeapon):
        super().__init__(weapon)

    def on_fire(self):
        print("Fired")
