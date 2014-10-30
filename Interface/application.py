#!/usr/bin/python3
# -*- coding:utf8 -*-

import sys

# from Running import Game
from main_widget import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.readSettings()

        self.setCentralWidget(MainWidget(self))

        self.createActions()
        self.createMenus()
        self.createStatusBar()

    def newGame(self):
        pass

    def openGame(self):
        pass

    def saveGame(self):
        pass

    def exitGame(self):
        pass

    def about(self):
        QtGui.QMessageBox.about(self, "About Application",
                                "Voila <b>voila</b>")

    def createActions(self):
        # File menu actions
        self.newGameAct = QAction("&New Game", self,
                                  statusTip="Create a new game",
                                  triggered=self.newGame)
        self.openGameAct = QAction("&Open Game", self,
                                   statusTip="Open an existing game",
                                   triggered=self.openGame)
        self.saveGameAct = QAction("&Save Game", self,
                                   statusTip="Save the current game",
                                   triggered=self.saveGame)
        self.exitGameAct = QAction("&Exit Game", self,
                                   statusTip="End the current game",
                                   triggered=self.exitGame)
        self.exitAct = QAction("E&xit the program", self,
                               statusTip="Return to linux",
                               triggered=self.close)

        # About menu actions
        self.aboutAct = QAction("&About", self,
                                statusTip="Show the application's About box",
                                triggered=self.about)
        self.aboutQtAct = QAction("About &Qt", self,
                                  statusTip="Show the Qt library's About box",
                                  triggered=qApp.aboutQt)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newGameAct)
        self.fileMenu.addAction(self.openGameAct)
        self.fileMenu.addAction(self.saveGameAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitGameAct)
        self.fileMenu.addAction(self.exitAct)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def createStatusBar(self):
        message = "Welcome in Shadows Empire !"
        self.statusBar().showMessage(message)

    def readSettings(self):
        settings = QSettings("Trolltech", "Application Example")
        self.WIN_WIDTH = 1280
        self.WIN_HEIGTH = 1024

        size = settings.value("size", QSize(self.WIN_WIDTH, self.WIN_HEIGTH))
        self.resize(size)

    def run(self):
        self.show()
        self.qtApp.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

app = MainWindow()
app.run()
