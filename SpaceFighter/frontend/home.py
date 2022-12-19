from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtCore import Qt
from .battleships import BattleShipUI
from .asteroids import AsteroidFactory


class MainUI(QWidget):
    _battle_ship = None
    _weapon = None
    _astroid_factory = None

    def __init__(self, *args, **kwargs):
        super().__init__(kwargs.get("parent"))
        self.initUI(*args, **kwargs)

    def initUI(self, *args, **kwargs):
        self.setWindowTitle("Warship Game")
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color: black;")

        self._battle_ship = BattleShipUI(parent=self, *args, **kwargs)
        # self._weapon = WeaponUI()
        # self._weapon.hide()
        self._astroid_factory = AsteroidFactory(parent=self)
        layout.addWidget(self._battle_ship, 0, 0, 0, 0)
        layout.addWidget(self._astroid_factory, 0, 10)

    def getWeapon(self):
        return self._weapon
