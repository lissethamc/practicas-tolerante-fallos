import sys

from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
