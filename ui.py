# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
from PyQt5 import QtCore, QtGui
import sys
from PIL import Image

class MyWidget(QWidget):
    def __init__(self, game_object=None):
        super().__init__()
        if not game_object:
            print("No game object found, probably debug mode")
        self.game_object = game_object
        self.layout = QVBoxLayout()
        ##TODO : set widget size dynamically, depending on image size
        button_icon = Image.open("./src/button_icon.jpg")
        image_height = button_icon.height
        image_width = button_icon.width
        button_stylesheet = """ 
            QWidget{
                color: white; 
                height: %s;
                width: %d;
                background-image: url("./src/button_icon.jpg"); 
                background-repeat: no-repeat; 
                background-position: center;
                border: none;
            }
        """ % (image_height, image_width)
        self.credit_button = QPushButton('Click')
        self.credit_button.setStyleSheet(button_stylesheet)
        self.layout.addWidget(self.credit_button)
        self.credit_button.clicked.connect(self.on_click)
        self.score_label = QLabel(str(self.game_object.credits_ects))
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
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
