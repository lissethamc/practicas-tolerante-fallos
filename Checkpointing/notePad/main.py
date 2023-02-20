import sys
import os

from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtTest
from apscheduler.schedulers.background import BackgroundScheduler


def autoSave():
    widget.statusBar().showMessage("autosaved!")
    QtTest.QTest.qWait(500)
    retrievedText = widget.plainTextEdit.toPlainText()
    #print(retrievedText)

    newFile = open("autosaved.txt","w")
    newFile.write(retrievedText)
    newFile.close()
    widget.statusBar().showMessage("")

def saveFile():
    retrievedText = widget.plainTextEdit.toPlainText()
    #print(retrievedText)
    newFile = open("notas.txt","w")
    newFile.write(retrievedText)
    newFile.close()

def retrieveText():
    if os.path.getsize('autosaved.txt') != 0:
        f = open("autosaved.txt","r")
        widget.plainTextEdit.setPlainText(f.read())
        #print(f.read()) 

def scheduledMethods():
    scheduler = BackgroundScheduler()
    scheduler.add_job(autoSave, 'interval', seconds=30)
    scheduler.start()

def newFile():
    widget.plainTextEdit.clear()

def is_closed():
    output = ("python3 main.py", "python main.py")[os.system("cd /home > nul 2>nul")] #0 for os.system command right, it means we're in linux
    os.system(f"{output}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    retrieveText()
    scheduledMethods()
    widget.show()
    widget.actionGuardar.triggered.connect(saveFile)
    widget.actionNuevo.triggered.connect(newFile)
    app.aboutToQuit.connect(is_closed)
    sys.exit(app.exec())
    