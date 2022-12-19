from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread, QObject, Qt, QSize
from PyQt5.QtGui import QPixmap
import time


class AstroidUI(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(kwargs.get("parent"))
        self.initUI()

    def initUI(self, *args, **kwargs):
        pxm = QPixmap(
            '/home/coder/Desktop/code/Projects/SpaceFighter/frontend/assets/img/asteroids/ast1.svg')
        pxm = pxm.scaled(100, 100, Qt.KeepAspectRatio)
        self.setPixmap(pxm)
        self.setFocus()


class Asteroid(QObject):
    layout = None

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.layout = kwargs.get("layout")

    def createObjects(self):
        pass
        # for i in range()
        # self.move(kwargs.get("dx"), kwargs.get('dy'))


class AsteroidFactory(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(kwargs.get('parent'))
        self.initUI(*args, **kwargs)
        # self.setStyleSheet("background-color: red;")

    def initUI(self, *args, **kwargs):
        pxm = QPixmap(
            '/home/coder/Desktop/code/Projects/SpaceFighter/frontend/assets/img/asteroids/ast1.svg')
        pxm = pxm.scaled(100, 100, Qt.KeepAspectRatio)
        self.setPixmap(pxm)
        self.setFixedSize(QSize(100, 100))
        self._thread = QThread()
        self._thread.start()

    def on_thread_start(self):
        parent = self.parentWidget()
        # asteroid = Asteroid(dx=parent.x(), dy=parent.y()-2)
        # parent.layout().addWidget(asteroid)
        # asteroid.moveToThread(self._thread)
