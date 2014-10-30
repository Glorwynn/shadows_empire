from PySide.QtCore import *
from PySide.QtGui import *


class TreeItem:
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return(self.childItems[row])

    def childCount(self):
        return(len(self.childItems))

    def columnCount(self):
        return(len(self.itemData))

    def data(self, column):
        try:
            return(self.itemData[column])
        except IndexError:
            return(None)

    def parent(self):
        return(self.parentItem)

    def row(self):
        if self.parentItem:
            return(self.parentItem.childItems.index(self))

        return(0)


class TreeModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.rootItem = TreeItem("Title", "Summary")
        self.setupModelData(data.split('\n'), self.rootItem)

    def columnCount(self, parent):
        if parent.isValid():
            return(parent.internalPointer().columnCount())
        else:
            return(self.rootItem.columnCount())

    def data(self, index, role):
        if not index.isValid():
            return(None)

        if role != Qt.DisplayRole:
            return(None)

        item = index.internalPointer()

        return(item.data(index.column()))

    def flags(self, index):
        if not index.isValid():
            return(Qt.NoItemFlags)

        return(Qt.ItemIsEnabled or Qt.ItemIsSelectable)

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return(self.rootItem.data(section))

        return(None)

    def index(self, row, colum, parent):
        if not self.hasIndex(row, colum, parent):
            return(QModelIndex())

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return(self.createIndex(row, column, childItem))
        else:
            return(QModelIndex())

    def parent(self, index):
        if not index.isValid():
            return(QModelIndex())

        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.rootItem:
            return(QtCore.QModelIndex())

        return(self.createIndex(parentItem.row(), 0, parentItem))


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
