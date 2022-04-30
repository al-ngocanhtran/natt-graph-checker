from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from graph import Visualization
import traceback


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Eulerian - Planar Graph Checker"
        top = 80
        left = 80
        width = 1000
        height = 600

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.label1 = QtWidgets.QLabel(
            "Instruction: The program will prompt user to input 2 vertices those connect to each other", self)
        self.label1.setGeometry(QtCore.QRect(170, 50, 900, 80))

        self.label2 = QtWidgets.QLabel(
            "Empty input", self)
        self.label2.setGeometry(QtCore.QRect(170, 350, 900, 80))


        self.listE = []
        self.MyUI()

    def MyUI(self):

        self.v1 = QPushButton("Enter Vertex 1", self)
        self.v1.setGeometry(QtCore.QRect(340, 200, 120, 28))

        self.textbox1 = QLineEdit(self)
        self.textbox1.setGeometry(QtCore.QRect(365, 250, 70, 28))

        self.v2 = QPushButton("Enter Vertex 2", self)
        self.v2.setGeometry(QtCore.QRect(500, 200, 120, 28))

        self.textbox2 = QLineEdit(self)
        self.textbox2.setGeometry(QtCore.QRect(525, 250, 70, 28))
        
        self.addMore = QPushButton("Add Edge", self)
        self.addMore.setGeometry(QtCore.QRect(380, 300, 100, 28))

        # if self.textbox1.text() != '' and self.textbox2.text() != '':
        #     print('Jump here')
        self.addMore.clicked.connect(self.updateInputs)
        # else:
        #     self.addMore.clicked.connect(self.raiseErr)

        self.finish = QPushButton("Finish", self)
        self.finish.setGeometry(QtCore.QRect(480, 300, 100, 28))
        self.finish.clicked.connect(self.finishInputs)

    ''' Still cannot handle err'''
    def raiseErr(self):

        if self.textbox1.text() == '' and self.textbox2.text() == '':
            err = "Please input the value of 2 vertices"
        elif self.textbox1.text() == '':
            err = "Please input the value of vertex 1"
        else:
            err = "Please input the value of vertex 2"

        msg = QMessageBox()
        msg.setWindowTitle("Input Error ")
        msg.setText(err)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.buttonClicked.connect(self.popupBtn)
        x = msg.exec_()

    def popupBtn(self, i):
        if i.text() == 'Cancel':
            self.textbox1.setText('')
            self.textbox2.setText('')
            return ''
        else:
            return self.textbox1.text()
        
    def updateInputs(self):
        self.listE.append([int(self.textbox1.text()),
                          int(self.textbox2.text())])
        count = 0
        mes = ''
        for pair in self.listE:
            if count != len(self.listE) - 1:
                mes += '[' + str(pair[0]) + ',' + str(pair[1]) + '],'
            else:
                mes += '[' + str(pair[0]) + ',' + str(pair[1]) + ']'
            count += 1
            
        self.label2.setText("Input:\n[" + mes + "]")
        self.textbox1.setText('')
        self.textbox2.setText('')
        print(self.listE)

    def finishInputs(self):

        if self.textbox1.text() != '' and self.textbox2.text() != '':
            self.listE.append([int(self.textbox1.text()),
                            int(self.textbox2.text())])
        self.textbox1.setText('')
        self.textbox2.setText('')
        canvas = Canvas(self, width=8, height=4, listE=self.listE)
        canvas.move(0, 0)
        
        self.label2.setText('Empty input')

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100, listE=[]):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot(listE)

    def plot(self, listE):
        Visualization.main(listE)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
