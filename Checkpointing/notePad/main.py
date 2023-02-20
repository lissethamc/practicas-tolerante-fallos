import sys
import os

from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from apscheduler.schedulers.background import BackgroundScheduler


def autoSave():
    retrievedText = widget.plainTextEdit.toPlainText()
    print(retrievedText)

    newFile = open("autosaved.txt","w")
    newFile.write(retrievedText)
    newFile.close()


def saveFile():
    retrievedText = widget.plainTextEdit.toPlainText()
    print(retrievedText)

    newFile = open("notas.txt","w")
    newFile.write(retrievedText)
    newFile.close()

def retrieveText():
    if os.path.getsize('autosaved.txt') != 0:
        f = open("autosaved.txt","r")
        widget.plainTextEdit.setPlainText(f.read())
        print(f.read()) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    retrieveText()
    scheduler = BackgroundScheduler()
    scheduler.add_job(autoSave, 'interval', seconds=30)
    scheduler.start()
    widget.show()
    widget.actionGuardar.triggered.connect(saveFile)
    sys.exit(app.exec())
