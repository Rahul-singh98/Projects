from PyQt5.QtCore import QObject


class IMovable(QObject):

    def moveTo(self, dx: int = 1, dy: int = 0):
        self.move(self.x() + dx, self.y() + dy)
