# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
from PyQt5 import QtCore, QtGui
import sys
from PIL import Image
from timeloop import Timeloop
from datetime import timedelta

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
        self.credit_button.clicked.connect(self.on_credit_click)
        self.score_label = QLabel(str(self.game_object.credits_ects))
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.professor_label = QLabel(str(self.game_object.professor) + " profs!")
        self.professor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.buy_professor_button = QPushButton("Adopte un prof!")
        self.buy_professor_button.clicked.connect(self.on_buy_professor_click)
        self.layout.addWidget(self.buy_professor_button)
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.professor_label)
        self.setLayout(self.layout)
        tl = Timeloop()
        @tl.job(interval=timedelta(seconds=10))
        def sample_job_every_10s():
            self.earn_upgrade_credits()
        tl.start()

        self.show()

    def on_credit_click(self):
        self.game_object.get_a_credit()
        self.score_label.setText(str(self.game_object.credits_ects))
        QApplication.processEvents()

    def on_buy_professor_click(self):
        if self.game_object.credits_ects >= 10:
            self.game_object.buy_a_professor()
            self.score_label.setText(str(self.game_object.credits_ects))
            self.professor_label.setText(str(self.game_object.professor) + " profs!")
            QApplication.processEvents()
        else:
            print("Not enough credits!")

    def earn_upgrade_credits(self):
        self.game_object.earn_upgrade_credits()
        self.score_label.setText(str(self.game_object.credits_ects))

    def closeEvent(self, *args, **kwargs):
        QtCore.QCoreApplication.processEvents()
        print("you just closed the pyqt window!!! you are awesome!!!")
        sys.exit()


def launch_widget(game_object):
    app = QApplication(sys.argv)
    ex = MyWidget(game_object)
    sys.exit(app.exec_())
