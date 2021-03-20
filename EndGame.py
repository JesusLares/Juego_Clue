import sys
from PyQt5.QtWidgets import QMessageBox, QStackedLayout, QComboBox, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

import Styles as sts
from data import data, tipoCosas
preguntas = ["¿Quien crees que es el asesino?",
             "¿Con que arma crees que fue?", "¿En que lugar crees que fue?"]
tipos = ["Personas", "Armas", "Lugares"]


class EndGame(QWidget):

    def __init__(self, moveMainFunction):
        super().__init__()
        self.moveMainFunction = moveMainFunction
        self.beginScreen()
        self.startUI()
        self.setLayout(self.stackedLayout)

    def beginScreen(self):
        self.stackedLayout = QStackedLayout()
        self.intro = QWidget()
        grid = QGridLayout()
        self.combos = []

        for i in range(3):
            label = QLabel(preguntas[i])
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setWordWrap(True)
            label.setStyleSheet(sts.style_title_result)
            self.combos.append(QComboBox(self))
            self.combos[i].addItems(tipoCosas[tipos[i]])
            self.combos[i].setStyleSheet(sts.style_combobox)
            self.combos[i].setEditable(True)
            self.combos[i].lineEdit().setAlignment(QtCore.Qt.AlignCenter)
            self.combos[i].lineEdit().setReadOnly(True)
            grid.addWidget(label, i*2, 0, 1, 3)
            grid.addWidget(self.combos[i], i*2+1, 1)

        button = QPushButton("Verificar")
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet(sts.style_buttons)
        button.clicked.connect(self.move)

        grid.addWidget(button, 6, 2)
        self.intro.setLayout(grid)
        self.stackedLayout.addWidget(self.intro)

    def startUI(self):
        self.result = QWidget()
        grid = QGridLayout()
        from data import histNumber
        cadena = "historia"+str(histNumber)
        self.history = data[cadena]
        
       
        self.titleLabel = QLabel("Fin del juego: " + 
                               self.history["ConclusionC"])
        
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet(sts.style_title)
        self.titleLabel.setWordWrap(True)
        

        buttonStart = QPushButton("Intentar de nuevo")
        buttonStart.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        buttonStart.setStyleSheet(sts.style_buttons)
        buttonStart.clicked.connect(self.startAgain)

        buttonE = QPushButton("Explicacion larga")
        buttonE.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        buttonE.setStyleSheet(sts.style_buttons)
        buttonE.clicked.connect(self.explication)

        grid.addWidget(self.titleLabel, 0, 0, 1, 3)
       # grid.addWidget(explainLabel, 1, 0)
        grid.addWidget(buttonE, 1, 0)
        grid.addWidget(buttonStart, 1, 2)

        self.result.setLayout(grid)
        self.stackedLayout.addWidget(self.result)

    def explication(self):
        #QMessageBox.information(self, "Explicacion",self.history["ConclusionL"])

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(
            "width:800px;QLabel{font-size: 20px;color:black;}")
        msg.setText("Explicacion Larga")
        msg.setText(self.history["ConclusionL"])
        msg.setWindowTitle("Explicacion")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def move(self):
        from data import histNumber
        cadena = "historia"+str(histNumber)
        self.history = data[cadena]
        self.titleLabel.setText("Fin del juego: " +
                                self.history["ConclusionC"])
        self.stackedLayout.setCurrentIndex(1)

    def startAgain(self):
        self.stackedLayout.setCurrentIndex(0)
        self.moveMainFunction(0)
