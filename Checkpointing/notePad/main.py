import sys

from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore


def saveFile():
    retrievedText = widget.plainTextEdit.toPlainText()
    print(retrievedText)

    newFile = open("notas.txt","w")
    newFile.write(retrievedText)
    newFile.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.actionGuardar.triggered.connect(saveFile)
    sys.exit(app.exec())
