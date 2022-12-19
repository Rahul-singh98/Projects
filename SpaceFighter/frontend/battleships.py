from backend.abstract import BaseShip, BaseWeapon
from backend.core import BattleShip, Missile
from PyQt5.QtWidgets import QLabel, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap


class BattleShipUI(QLabel):
    _battle_ship = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI(*args, **kwargs)

    def initUI(self, *args, **kwargs):
        self._battle_ship = BattleShip(Missile)
        pxm = QPixmap(
            '/home/coder/Desktop/code/Projects/SpaceFighter/frontend/assets/img/spaceship_blue.svg')
        pxm = pxm.scaled(100, 100, Qt.KeepAspectRatio)
        self.setPixmap(pxm)
        self.setFocus()
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(QSize(100, 100))
        # self.setStyleSheet("background-color: green;")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            if (self.y() - 5 >= 0):
                self.move(self.x(), self.y() - 5)
        elif event.key() == Qt.Key_Down:
            if (self.y() + 5 <= self.parentWidget().height() - 100):
                self.move(self.x(), self.y() + 5)
        elif event.key() == Qt.Key_Left:
            if self.x() - 5 > 0:
                self.move(self.x() - 5, self.y())
        elif event.key() == Qt.Key_Right:
            if self.x() + 5 <= self.parentWidget().width() - 100:
                self.move(self.x() + 5, self.y())
        elif event.key() == Qt.Key_Space:
            self._battle_ship.on_fire()
            # self.fire()
            # self.parentWidget().getWeapon().on_fire(1, 0)
        self.isChildAt(self.x(), self.y())

    # def fire(self):
    #     ui = WeaponUI(parent=self)
    #     ui.on_fire(self.x(), self.y())

    def isChildAt(self, x, y):
        if self.childAt(x, y) != None:
            print("Overlay")

    def setBattleShip(self, battleship: BaseShip):
        self._battle_ship = battleship

    def setWeapon(self, weapon: BaseWeapon):
        self._battle_ship.setWeapon(weapon)
