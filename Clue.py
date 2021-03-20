import sys
from PyQt5.QtWidgets import QStackedLayout, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import Styles as sts
from StartGame import StartGame
from EndGame import EndGame

from data import editHistNumber
from random import randint


class Clue(QWidget):

    def __init__(self):
        super().__init__()
        self.beginScreen()
        self.startUI()
        self.show()

    def beginScreen(self):
        self.stackedLayout = QStackedLayout()
        self.setWindowTitle('Clue')
        self.move(700, 200)
        self.setFixedWidth(1000)
        self.setFixedHeight(500)
        self.setStyleSheet("background:"+sts.color_primary)

    def startUI(self):
        self.start = QWidget()
        grid = QGridLayout()

        titleLabel = QLabel("¿Podras saber quien fue el asesino?")
        titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        titleLabel.setStyleSheet(sts.style_title)

        buttonStart = QPushButton("Iniciar")
        buttonStart.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        buttonStart.setStyleSheet(sts.style_button_start)
        buttonStart.clicked.connect(self.startGame)

        grid.addWidget(titleLabel, 0, 0)
        grid.addWidget(buttonStart, 1, 0)
        self.start.setLayout(grid)

        self.stackedLayout.addWidget(self.start)

        self.game = StartGame(self.moveMainFunction)
        self.stackedLayout.addWidget(self.game)

        self.end = EndGame(self.moveMainFunction)
        self.stackedLayout.addWidget(self.end)

        self.setLayout(self.stackedLayout)

    def startGame(self):
        self.moveMainFunction(1)

    def moveMainFunction(self, index):
        if index == 0:
            editHistNumber()
        self.stackedLayout.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = Clue()
    application.show()
    sys.exit(app.exec_())
