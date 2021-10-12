from PyQt5 import QtCore,QtWidgets,QtGui
from sys import argv

class Animation(QtWidgets.QWidget):
    def __init__(self):
        super(Animation, self).__init__()
        self.setStyleSheet("background-color: black;")
        self.setWindowIcon(QtGui.QIcon("3.jpg"))
        self.setWindowTitle("Let's Animate Together")
        self.setFixedSize(600,600)

        self.window2 = QtWidgets.QWidget(self)
        self.window2.setFixedSize(100,100)
        self.window2.setStyleSheet("background-color: orange;")
        self.animation1 = QtCore.QPropertyAnimation(self.window2,b"pos")
        self.animation1.setEndValue(QtCore.QPoint(600 - 100, 600 - 100))
        self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.animation1.setDuration(2000)
        self.animation1.setLoopCount(-1)
        self.animation1.start()

        self.window3 = QtWidgets.QWidget(self)
        self.window3.setFixedSize(100, 100)
        self.window3.move(600-100,0)
        self.window3.setStyleSheet("background-color: orange;")
        self.animation2 = QtCore.QPropertyAnimation(self.window3, b"pos")
        self.animation2.setEndValue(QtCore.QPoint(0, 600 - 100))
        self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.animation2.setDuration(2000)
        self.animation2.setLoopCount(-1)
        self.animation2.start()

        self.window4 = QtWidgets.QWidget(self)
        self.window4.setFixedSize(100, 100)
        self.window4.move(600 - 100, 600 - 100)
        self.window4.setStyleSheet("background-color: orange;")
        self.animation3 = QtCore.QPropertyAnimation(self.window4, b"pos")
        self.animation3.setEndValue(QtCore.QPoint(0, 0))
        self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.animation3.setDuration(2000)
        self.animation3.setLoopCount(-1)
        self.animation3.start()

        self.window5 = QtWidgets.QWidget(self)
        self.window5.setFixedSize(100, 100)
        self.window5.move(0, 500)
        self.window5.setStyleSheet("background-color: orange;")
        self.animation4 = QtCore.QPropertyAnimation(self.window5, b"pos")
        self.animation4.setEndValue(QtCore.QPoint(500,0))
        self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.animation4.setDuration(2000)
        self.animation4.setLoopCount(-1)
        self.animation4.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    anim = Animation()
    anim.show()
    app.exec_()