from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
from PyQt5 import QtCore
import sys


class MyWidget(QWidget):
    def __init__(self, game_object=None):
        super().__init__()
        if not game_object:
            print("No game object found, probably debug mode")
        self.game_object = game_object
        self.layout = QVBoxLayout()
        self.credit_button = QPushButton('Click')
        self.layout.addWidget(self.credit_button)
        self.credit_button.clicked.connect(self.on_click)
        self.score_label = QLabel(str(self.game_object.credits_ects))
        self.layout.addWidget(self.score_label)
        self.setLayout(self.layout)
        self.show()

    def on_click(self):
        self.game_object.get_a_credit()
        self.score_label.setText(str(self.game_object.credits_ects))
        QApplication.processEvents()

    def closeEvent(self, *args, **kwargs):
        QtCore.QCoreApplication.processEvents()
        print("you just closed the pyqt window!!! you are awesome!!!")
        sys.exit()


def launch_widget(game_object):
    app = QApplication(sys.argv)
    ex = MyWidget(game_object)
    sys.exit(app.exec_())
