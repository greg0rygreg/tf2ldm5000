import random
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import clipboard
import numpy as np

def inargs(arg):
    return True if arg in sys.argv else False

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("app.ui", self)
        self.show()
        if inargs("-debug"):
            print("debug on")
        # remember, code here
        # functions are OUT of __init__
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.pushButton.clicked.connect(self.genld)
        self.pushButton_2.clicked.connect(self.copy)
    def genld(self):
        # thanks podemb
        if (game := self.game_cbox.currentText()) == "Vanilla":
            with open('loadouts all.txt' if not self.checkBox.isChecked() else 'loadouts nocosre.txt', 'r') as f:
                loadouts = f.read().split('\n\n')
                for i, loadout in enumerate(loadouts):
                    loadouts[i] = loadout.split("\n")
        # 2d list [['SCOUT', ..], ['SOLDIER', ..], ..]
        for loadout in loadouts:
            if loadout[0].lower() == self.merc_cbox.currentText().lower():
                chosen = loadout
                break
        # list ['SCOUT', ..]
        chosen_l = random.choice(chosen)
        while chosen_l == chosen[0]:
            chosen_l = random.choice(chosen)
        # string 'Scattergun, ...'
        split_l = chosen_l.split(", ")
        # list ['Scattergun', ...]


        if inargs("-debug"):
            print(chosen)
        # no it doesnt need fixing, it needs removing (no more -saveongen argument, ya got the fuckin loadouts all.txt file smartypants.)
        
        self.label.setText(f"Game: {self.game_cbox.currentText()}\nMerc: {self.merc_cbox.currentText()}\nPrimary: {split_l[0]}\nSecondary: {split_l[1]}\nMelee: {split_l[2]}\nPDA: {split_l[3]}\n({len(chosen) - 2} more loadouts available)")
    def copy(self):
        clipboard.copy(f"""This is my automatically generated loadout, done with TF2 Loadout Maker 5000\n{self.label.text()}\nDownload TF2 Loadout Maker 5000 from https://gitlab.com/tf2-based/team-fortress-2-loadout-maker-5000""")
        msgbox = QMessageBox()
        msgbox.setText("Thanks for using TF2 Loadout Maker 5000!")
        msgbox.setWindowIcon(QtGui.QIcon("icon.ico"))
        msgbox.setIcon(QMessageBox.Icon.Information)
        msgbox.setWindowTitle("Thanks!")
        msgbox.exec_()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
