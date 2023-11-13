import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circle)
        self.draw = False

    def paintEvenrt(self, pe) -> None:
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            d = random.randint(1, min(self.width(), self.height()))
            rect = QRect(random.randint(0, self.width() - d),
                         random.randint(0, self.height() - d),
                         d, d)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(rect)
            qp.end()
            self.draw = False

    def circle(self):
        self.draw = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
