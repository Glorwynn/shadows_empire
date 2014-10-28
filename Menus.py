from PySide.QtCore import *
from PySide.QtGui import *


class FileMenu(QMenu):

    def __init__(self, parent):
        QMenu.__init__(self, "&File")
        self.parent = parent

        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(self.parent.qtApp.quit)

        self.addAction(exitAction)


class AboutMenu(QMenu):
    def __init__(self, parent):
        QMenu.__init__(self, "&About")
        self.parent = parent

        infoAction = QAction('More &Information', self)
        infoAction.triggered.connect(self.infos)

        self.addAction(infoAction)

    @Slot()
    def infos(self):
        self.mBox = QMessageBox(self.parent)
        self.mBox.setText("More informations coming soon !")
        self.mBox.exec_()
