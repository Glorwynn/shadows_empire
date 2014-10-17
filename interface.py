#!/usr/bin/python3

import sys

from PySide.QtCore import *
from PySide.QtGui import *

qtApp = QApplication(sys.argv)


class MainWindow(QWidget):
    def __init__(self):
        self.WIN_WIDTH = 1280
        self.WIN_HEIGTH = 1024
        self.TABLE_FONT = QFont("Helvetica", 14, QFont.Bold)
        self.x = 5
        self.y = 5
        self.list_instr = []

        QWidget.__init__(self)
        self.setWindowTitle("Fête de la science")
        self.setMinimumSize(QSize(self.WIN_WIDTH, self.WIN_HEIGTH))

        self.global_layout = QVBoxLayout()
        self.upper_layout = QHBoxLayout()

        self.upper_layout.addStretch(1)
        self.left_layout = QVBoxLayout()
        self.left_layout.addStretch(1)

        self.grid = QTableWidget(8, 8, self)
        self.grid.setMinimumSize(482, 482)
        for row in range(0, 8):
            for col in range(0, 8):
                self.grid.setRowHeight(row, 60)
                self.grid.setColumnWidth(col, 60)

                item = QTableWidgetItem()
                item.setBackground(Qt.white)
                item.setForeground(Qt.black)
                item.setFont(self.TABLE_FONT)
                self.grid.setItem(row, col, item)

        self.grid.horizontalHeader().hide()
        self.grid.verticalHeader().hide()

        self.left_layout.addWidget(self.grid)
        self.left_layout.addStretch(1)
        self.upper_layout.addLayout(self.left_layout)

        self.upper_layout.addStretch(1)

        self.right_layout = QVBoxLayout()
        self.right_layout.addStretch(1)

        self.butt_layout = QFormLayout()
        self.bt_front = QPushButton("Front", self)
        self.bt_front.clicked.connect(self.push_front)
        self.bt_back = QPushButton("Back", self)
        self.bt_back.clicked.connect(self.push_back)
        self.bt_left = QPushButton("Left", self)
        self.bt_left.clicked.connect(self.push_left)
        self.bt_right = QPushButton("Right", self)
        self.bt_right.clicked.connect(self.push_right)

        self.bt_go = QPushButton("Lancer le programme !", self)
        self.bt_go.clicked.connect(self.move)

        self.butt_layout.addRow(self.bt_front, self.bt_back)
        self.butt_layout.addRow(self.bt_left, self.bt_right)
        self.right_layout.addLayout(self.butt_layout)
        self.right_layout.addWidget(self.bt_go)
        self.right_layout.addStretch(1)

        self.upper_layout.addLayout(self.right_layout)
        self.global_layout.addLayout(self.upper_layout)

        self.text_zone = QTextEdit(self)
        self.text_zone.setReadOnly(True)
        self.global_layout.addWidget(self.text_zone)

        self.setLayout(self.global_layout)

    @Slot()
    def push_front(self):
        self.text_zone.append("pl.avance()")
        self.list_instr += ["front"]

    @Slot()
    def push_back(self):
        self.text_zone.append("pl.recule()")
        self.list_instr += ["back"]

    @Slot()
    def push_left(self):
        self.text_zone.append("pl.gauche()")
        self.list_instr += ["left"]

    @Slot()
    def push_right(self):
        self.text_zone.append("pl.droite()")
        self.list_instr += ["right"]

    @Slot()
    def move(self):
        for instr in self.list_instr:
            if instr == "front":
                self.grid.item(self.x, self.y).setText("")
                self.x -= 1
                self.grid.item(self.x, self.y).setText("O")
            elif instr == "back":
                self.grid.item(self.x, self.y).setText("")
                self.x += 1
                self.grid.item(self.x, self.y).setText("O")
            elif instr == "left":
                self.grid.item(self.x, self.y).setText("")
                self.y -= 1
                self.grid.item(self.x, self.y).setText("O")
            elif instr == "right":
                self.grid.item(self.x, self.y).setText("")
                self.y += 1
                self.grid.item(self.x, self.y).setText("O")

    def run(self):
        self.show()
        self.grid.item(self.x, self.y).setText("O")
        qtApp.exec_()

app = MainWindow()
app.run()
