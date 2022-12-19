from backend.core import Missile
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class WeaponUI(QLabel):
    _weapon = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI(*args, **kwargs)

    def initUI(self, *args, **kwargs):
        self._weapon = Missile()
        pxm = QPixmap(
            '/home/coder/Desktop/code/Projects/SpaceFighter/frontend/assets/img/Rocket8.svg')
        pxm = pxm.scaled(100, 100, Qt.KeepAspectRatio)
        self.setPixmap(pxm)

    def on_fire(self, x_incr: 2, y_incr: 0):
        while True:
            self.move(self.x() + x_incr, self.y() + y_incr)


class WeaponFactory:
    _max_weapons = 1000
    