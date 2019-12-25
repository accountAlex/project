import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import uic

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

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
        'champion': 'чемпион',
        'dream': 'мечта',
        'team': 'команда',
        'home': 'дом'
        }

spisok = ['машина', 'вокруг', 'середина', 'кровать', 'море', 'песня', 'год', 'музыка', 'окно']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pro1.ui', self)
        self.buttons = [self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.titles = set()
        self.Start.clicked.connect(self.clear_and_start)
        self.pushButton_2.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.check)
        self.pushButton_4.clicked.connect(self.check)
        self.pushButton_5.clicked.connect(self.check)
        
    def clear_and_start(self):
        self.count = 0
        self.run()
        
    def run(self):
        self.titles.clear()
        self.flag = 0
        self.label.setText(random.choice(list(words.keys())))
        self.label_2.setText(str(self.count))
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
                
    def check(self):
        if self.sender().text() == words[self.label.text()]:
            self.count += 1
            self.label_2.setText(str(self.count))
        self.run()
        
        
        

sys.excepthook = except_hook
app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
