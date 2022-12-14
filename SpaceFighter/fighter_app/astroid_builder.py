from abc import ABC
import random
import json


class AstroidBase(ABC):
    _x = 0
    _y = 0
    _height = 0
    _wight = 0
    _immunity = 0
    _src = ""

    def __init__(self, x: int = 0, y: int = 0, height: int = 0, width: int = 0, immunity: int = 100, img_src=""):
        self._x = x
        self._y = y
        self._height = height
        self._wight = width
        self._immunity = immunity
        self._src = img_src

    def setPosition(self, x, y):
        self._x = x
        self._y = y

    def decrPlace(self):
        self._y -= 3

    def getPosition(self):
        return [self._x, self._y]

    def attackedBy(self, x):
        self._immunity -= x
        if self._immunity <= 0:
            self.onImmunity()

    def onImmunity(self):
        pass

    def getData(self):
        return {
            "x": self._x,
            "y": self._y,
            "height": self._height,
            "width": self._wight,
            "health": self._immunity,
            "img_src": self._src,
        }


class SimpleAsteroid(AstroidBase):

    def __init__(self, h, w):
        x = w
        y = random.randint(0, h-1)
        height = random.randint(20, 100)
        width = random.randint(20, 100)
        immunity = random.randint(50, 150)

        img_path = f"/static/img/asteroids/ast{random.randint(1, 6)}.svg" 

        super().__init__(x-width, y-height, height, width, immunity, img_path)


class AsteroidBuilder:

    def __init__(self, size: int = 10, h: int=100, w: int=100):
        self._size = size
        self._asteroids_list = []
        for i in range(size):
            self._asteroids_list.append(SimpleAsteroid(h, w))

    def getAllAstroids(self):
        return self._asteroids_list

    def getAllCoordinates(self):
        data_dict = {'asteroids': []}
        for obj in self._asteroids_list:
            obj_dict = obj.getData()
            if obj_dict.get('health') <= 0:
                continue
            data_dict["asteroids"].append(obj_dict)
            obj.decrPlace()
        return data_dict
