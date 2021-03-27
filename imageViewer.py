#!/usr/bin/env python3
import sys
import pathlib
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QMessageBox, QApplication, QLabel


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Ofer\'s App'
        self.width = 1280
        self.height = 1024
        self.initUI()
        self.i = 0
        self.j = 0
        self.count = 0
        self.path = [str(pathlib.Path().absolute()) + "\\1.png",
                     str(pathlib.Path().absolute()) + "\\2.png",
                     str(pathlib.Path().absolute()) + "\\3.png"]

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.button1 = QPushButton('1', self)
        self.button1.move(40, 20)
        self.button1.resize(100, 100)
        self.button1.clicked.connect(self.exitApp)

        self.button2 = QPushButton('2', self)
        self.button2.move(440, 800)
        self.button2.resize(280, 120)
        self.button2.clicked.connect(self.saveImage)

        self.button3 = QPushButton('3', self)
        self.button3.move(1000, 190)
        self.button3.resize(220, 120)
        self.button3.clicked.connect(self.displayImages)

        self.label = QLabel(self)
        self.label.move(10, 50)

        self.show()

    def displayImages(self):
        self.count = 1

        self.addButton()

        imagePathNew = self.path[self.i]
        self.pixmap = QPixmap(imagePathNew)
        self.pixmap = self.pixmap.scaled(850, 600)
        self.label.setPixmap(self.pixmap)
        self.label.move(140, 190)
        self.label.adjustSize()
        self.i += 1
        if self.i >= 2:
            self.i = 2

    def addButton(self):
        self.j += 1
        if self.j > 1:
            self.button4.hide()
        self.button4 = QPushButton('4', self)
        self.button4.move(1000, 320)
        self.button4.resize(220, 120)
        self.button4.show()
        self.button4.clicked.connect(self.deleteButton)

    def deleteButton(self):
        self.button4.hide()
        self.pixmap = QPixmap(self.path[0])
        self.pixmap = self.pixmap.scaled(850, 600)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()
        self.i = 1

    def saveImage(self):
        if self.count != 0:
            filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                      "BMP(*.bmp);;All Files(*.*) ")
            self.pixmap.save(filePath)
        else:
            QMessageBox.about(self, "Error", "No images loaded!")

    def exitApp(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
