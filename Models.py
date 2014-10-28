from PySide.QtCore import *
from PySide.QtGui import *


class TeamModel(QStandardItemModel):
    def __init__(self, leader, members):
        QStandardItemModel.__init__(self)
        self._leader = QStandardItem(leader)
        self._members = [QStandardItem(member) for member in members]
        self.appendRow(self._leader)
        for member in self._members:
            self._leader.appendRow(member)
