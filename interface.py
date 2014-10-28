#!/usr/bin/python3
# -*- coding:utf8 -*-

import sys

from MainWidget import *
from Menus import *


class MainWindow(QMainWindow):
    def __init__(self):
        # Constants
        self.WIN_WIDTH = 1280
        self.WIN_HEIGTH = 1024
        self.qtApp = QApplication(sys.argv)

        # Window initialization
        QMainWindow.__init__(self)
        self.setWindowTitle("Shadows empire")
        self.setMinimumSize(QSize(self.WIN_WIDTH, self.WIN_HEIGTH))

        # Interface construction
        self.initUI()

    def initUI(self):
        # Menu bar
        self.menuBar().addMenu(FileMenu(self))
        self.menuBar().addMenu(AboutMenu(self))

        # Tool bar

        # Central widget
        self.setCentralWidget(MainWidget(self))

        # Status bar
        self.statusBar()

    def run(self):
        self.show()
        self.qtApp.exec_()

app = MainWindow()
app.run()
