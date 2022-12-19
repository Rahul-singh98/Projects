from PyQt5.QtWidgets import QApplication
from frontend import home
import sys


if __name__ == "__main__":
    application = QApplication(["Free Game"])
    widget = home.MainUI()
    widget.showMaximized()

    sys.exit(application.exec())