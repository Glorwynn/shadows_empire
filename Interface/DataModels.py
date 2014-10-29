from PySide.QtCore import *
from PySide.QtGui import *


class OrganisationTree(QTreeWidget):
    headers = ["Nom", "Niveau", "Domaine de crime"]
    #interested = Signal(str)

    def __init__(self, parent, leader, members):
        QTreeWidget.__init__(self)
        self.parent = parent
        self.setColumnCount(3)
        self.setHeaderLabels(self.headers)

        self._leader = leader

        self._leader_item = QTreeWidgetItem(self)
        self._leader_item.setText(0, self._leader)

        for member in members:
            self._members = QTreeWidgetItem(self._leader_item)
            for i in range(len(member)):
                self._members.setText(i, member[i])

            if member[2] == "Vol":
                self._members.setForeground(0, QColor(Qt.green))
            elif member[2] == "Assassinat":
                self._members.setForeground(0, QColor(Qt.red))
            elif member[2] == "Prostitution":
                self._members.setForeground(0, QColor(Qt.blue))
            elif member[2] == "Contrebande":
                self._members.setForeground(0, QColor(Qt.gray))

        self.itemClicked.connect(self.parent.details_box.display)
        #self.interested.connect(self.parent.details_box.display)

    @Slot()
    def punch(self):
        self.interested.emit("Blabla")


class BuildingsTree(QTreeWidget):
    headers = ["Nom", "Taille"]

    def __init__(self, parent, leader, members):
        QTreeWidget.__init__(self)
        self.parent = parent
        self.setColumnCount(2)
        self.setHeaderLabels(self.headers)

        self._leader = QTreeWidgetItem(self)
        self._leader.setText(0, leader)
        #self._leader.setForeground(0, QColor(Qt.red))

        for member in members:
            self._members = QTreeWidgetItem(self._leader)
            self._members.setText(0, member)
