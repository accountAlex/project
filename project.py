# -*- coding: utf-8 -*-
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QColor, QLineEdit
from PyQt5 import uic

words = {
        'car': 'машина',
        'around': 'вокруг',
        'midle': 'середина',
        'bed': 'кровать',
        'sea': 'море',
        'song': 'песня',
        'year': 'год',
        'music': 'музыка',
        'window': 'окно',
        }

spisok = ['машина', 'вокруг', 'середина', 'кровать', 'море', 'песня', 'год', 'музыка', 'окно']

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pro1.ui', self)
        self.buttons = [self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.titles = set()
        self.pushButton.clicked.connect(self.run)
        
    def run(self):
        self.titles.clear()
        self.flag = 0
        self.label.setText(random.choice(list(words.keys())))
        for i in self.buttons:
            number = random.randint(0, 100)
            if ((number in range(80, 100)) or (i == self.pushButton_5)) and (not(self.flag)):
                i.setText(words[self.label.text()])
                self.titles.add(words[self.label.text()])
                self.flag = 1
            else:
                n = random.choice(spisok)
                while n in self.titles or n == words[self.label.text()]:
                    n = random.choice(spisok)
                i.setText(n)
                self.titles.add(n)