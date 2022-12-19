import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Mover(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QtGui.QPixmap('/home/coder/Desktop/code/Projects/SpaceFighter/frontend/assets/img/spaceship_blue.svg'))
        self.setGeometry(0, 0, 200, 200)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.move(self.x(), self.y() - 5)
        elif event.key() == QtCore.Qt.Key_Down:
            self.move(self.x(), self.y() + 5)
        elif event.key() == QtCore.Qt.Key_Left:
            self.move(self.x() - 5, self.y())
        elif event.key() == QtCore.Qt.Key_Right:
            self.move(self.x() + 5, self.y())
        else:
            QtWidgets.QLabel.keyPressEvent(self, event)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)
        self.mover = Mover(centralWidget)
        self.mover.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())