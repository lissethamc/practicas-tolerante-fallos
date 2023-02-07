# This Python file uses the following encoding: utf-8
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import os

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        path=os.path.abspath("form.ui")
        uic.loadUi(path, self)

