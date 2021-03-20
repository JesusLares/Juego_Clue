import sys
from PyQt5.QtWidgets import QStackedLayout, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import Styles as sts
from data import data, tipoCosas

introduccion = """Informacion inicial: Eres el detective que investiga el caso de la muerte del esposo
        * Deberas analizar con detenimiento cada texto  que te otorge tu seleccion ya que seguramente te daran pista de quien fue el asesino
        *Cuentas con un numero limitado de preguntas asi que intenta ser preciso
"""


class StartGame(QWidget):

    def __init__(self, moveMainFunction):
        super().__init__()
        self.moveMainFunction = moveMainFunction

        self.numberQuestion = 0
        self.BeginScreen()
        self.ChooseType()
        self.SelectInfo()
        self.moveGameFunction(0)
        self.setLayout(self.stackedLayout)

    def BeginScreen(self):
        self.stackedLayout = QStackedLayout()
        self.intro = QWidget()
        grid = QGridLayout()

        self.introLabel = QLabel(introduccion)
        self.introLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.introLabel.setWordWrap(True)
        self.introLabel.setStyleSheet(sts.style_title)

        self.buttonIntro = QPushButton("Estoy listo")
        self.buttonIntro.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonIntro.setStyleSheet(sts.style_button_start)
        self.buttonIntro.clicked.connect(self.MoveChooseType)
        
        self.buttonFinish = QPushButton("Tengo respuesta")
        self.buttonFinish.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonFinish.setStyleSheet(sts.style_button_start)
        self.buttonFinish.clicked.connect(self.FindOut)
        self.buttonFinish.setVisible(False)

        grid.addWidget(self.introLabel, 0, 0, 1, 3)
        grid.addWidget(self.buttonIntro, 1, 2)
        
        grid.addWidget(self.buttonFinish, 1, 1)
        
        self.intro.setLayout(grid)

        self.stackedLayout.addWidget(self.intro)

    def ChooseType(self):
        self.chooseType = QWidget()
        self.numberQT = QLabel("1/10")
        self.numberQT.setStyleSheet(sts.style_Noquestion)

        tipo = ["Personas", "Armas", "Lugares"]
        grid = QGridLayout()
        question = QLabel(
            "¿Que tipo de información deseas obtener?")
        question.setAlignment(QtCore.Qt.AlignCenter)
        question.setWordWrap(True)
        question.setStyleSheet(sts.style_question)

        grid.addWidget(self.numberQT, 0, 2)
        grid.addWidget(question, 1, 0, 1, 3)
     
        buttons = []
        for i in tipo:
            buttons.append(self.createButtons(i, self.MoveSelectInfo))

        self.adjustButtons(len(buttons), grid, buttons)

        self.chooseType.setLayout(grid)
        self.stackedLayout.addWidget(self.chooseType)

    def SelectInfo(self):
        self.selectInfo = QWidget()
        info = ["", "", "", "", ""]
        grid = QGridLayout()
        self.numberQS = QLabel("1/10")
        self.numberQS.setStyleSheet(sts.style_Noquestion)
        self.questionInfo = QLabel("")
        self.questionInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.questionInfo.setWordWrap(True)
        self.questionInfo.setStyleSheet(sts.style_question)

        grid.addWidget(self.numberQS, 0, 2)
        grid.addWidget(self.questionInfo, 1, 0, 1, 3)
        self.buttonsInfo = []
        for i in info:
            self.buttonsInfo.append(
                self.createButtons(i, self.MoveBeginScreen))

        self.adjustButtons(len(self.buttonsInfo), grid, self.buttonsInfo)

        self.selectInfo.setLayout(grid)
        self.stackedLayout.addWidget(self.selectInfo)

    def MoveBeginScreen(self, selection):
        from data import histNumber
        cadena = "historia"+str(histNumber)
        self.introLabel.setText(data[cadena][selection])
        self.numberQuestion += 1
        
        self.buttonFinish.setVisible(True)

        cadena = "Continuar"
        if self.numberQuestion >= 10:
            cadena = "Finalizar"
        self.buttonIntro.setText(cadena)
        self.moveGameFunction(0)

    def MoveChooseType(self, ok):
        if self.numberQuestion >= 10:
            self.numberQuestion = 0
            self.numberQT.setText(str(self.numberQuestion+1)+"/10")
            self.numberQS.setText(str(self.numberQuestion+1)+"/10")
            self.moveGameFunction(0)
            self.moveMainFunction(2)
            self.introLabel.setText(introduccion)
            cadena = "Estoy listo"
            self.buttonIntro.setText(cadena)
            self.buttonFinish.setVisible(False)
        else:
            self.numberQT.setText(str(self.numberQuestion+1)+"/10")
            self.numberQS.setText(str(self.numberQuestion+1)+"/10")
            self.moveGameFunction(1)
            
    def FindOut(self):
        self.numberQuestion = 0
        self.numberQT.setText(str(self.numberQuestion+1)+"/10")
        self.numberQS.setText(str(self.numberQuestion+1)+"/10")
        self.moveGameFunction(0)
        self.moveMainFunction(2)
        self.introLabel.setText(introduccion)
        cadena = "Estoy listo"
        self.buttonIntro.setText(cadena)
        self.buttonFinish.setVisible(False)

    def MoveSelectInfo(self, type):
        self.questionInfo.setText(
            "¿Sobre que "+type.lower()+" deseas obtener información?")
        for i in range(5):
            self.buttonsInfo[i].setText(tipoCosas[type][i])
        self.moveGameFunction(2)

    def createButtons(self, answer, function):
        button = QPushButton(answer)
        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setFixedWidth(300)
        button.setStyleSheet(sts.style_buttons)
        button.clicked.connect(
            lambda x: self.pressButtonAnswer(button, function))
        return button

    def pressButtonAnswer(self, answer_btn, function):
        function(answer_btn.text())

    def adjustButtons(self, noButtons, grid, buttons):
        row = 0
        column = 2
        for i in range(noButtons):
            grid.addWidget(buttons[i], column, row)
            row += 1
            if row == 3:
                row = 0
                column += 1

    def moveGameFunction(self, index):
        self.stackedLayout.setCurrentIndex(index)
