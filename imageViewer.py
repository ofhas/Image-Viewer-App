#!/usr/bin/env python3
import sys
import pathlib
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog, QMessageBox, QApplication, QLabel


class App(QWidget):
    # we'll use super to avoid referring to the base class explicitly and the use of multiply inheritance we'll also
    # use pathlib in order to get the .py file path automatically without the need to change it on every time
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

    # in this method we'll create and position the buttons of the app, also well define each button functionality i.e(connecting it to it's method), and create the main window,
    #
    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.button1 = QPushButton('#1', self)
        self.button1.move(224, 20)
        self.button1.resize(100, 100)
        self.button1.clicked.connect(self.exitApp)

        self.button2 = QPushButton('#2', self)
        self.button2.move(512, 800)
        self.button2.resize(280, 120)
        self.button2.clicked.connect(self.saveImage)

        self.button3 = QPushButton('#3', self)
        self.button3.move(1000, 256)
        self.button3.resize(220, 120)
        self.button3.clicked.connect(self.displayImages)

        self.label = QLabel(self)
        self.label.move(10, 50)

        self.show()

    # here we'll create the images display method by using an index(self.i) that each time the button 3 is pressed the
    # image index changes causing it to move to the next one after until we get to the last index which stays at the
    # value 2 which displays the third image, we'll also call the method that creates button 4, as it should appear
    # when button 3 is pressed
    def displayImages(self):
        self.count = 1

        self.addButton()

        imagePathNew = self.path[self.i]
        self.pixmap = QPixmap(imagePathNew)
        self.pixmap = self.pixmap.scaled(640, 512)
        self.label.setPixmap(self.pixmap)
        self.label.move(320, 256)
        self.label.adjustSize()
        self.i += 1
        if self.i >= 2:
            self.i = 2

    # in this method we'll create button 4 dynamically after button 3 is pressed and present the first image,
    # when pressing button 4 it delete the button but at the same time calls the the display Images method that again
    # creates button 4 again, in order to delete the newly unwanted button 4 we'll use the hide() and by checking if
    # self.j is bigger than 1 which means another button 4 is created as a result the button will be hidden
    def addButton(self):
        self.j += 1
        if self.j > 1:
            self.button4.hide()
        self.button4 = QPushButton('#4', self)
        self.button4.move(1000, 380)
        self.button4.resize(220, 120)
        self.button4.show()
        self.button4.clicked.connect(self.deleteButton)

    def deleteButton(self):
        self.button4.hide()
        self.pixmap = QPixmap(self.path[0])
        self.pixmap = self.pixmap.scaled(640, 512)
        self.label.setPixmap(self.pixmap)
        self.label.adjustSize()
        self.i = 1
# here we'll create the method that enables to save the current image to a bmp file by using the self.pixmap that was
    # created on the displayImages method error handling is also define here in case the user didn't press button 3
    # and no image is presented, if doing so the user should get a message saying no images are loaded
    def saveImage(self):
        if self.count != 0:
            filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                      "BMP(*.bmp);;All Files(*.*) ")
            self.pixmap.save(filePath)
        else:
            QMessageBox.about(self, "Error", "No images loaded!")
# here well define the method the enables the exits the window by using the built in exit method

    def exitApp(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
