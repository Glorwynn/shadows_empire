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

    def setData(self, column, value):
        if column < 0 or column >= len(self.itemData):
            return(False)

        self.itemData[column] = value

        return(True)


class OrganizationTreeModel(QAbstractItemModel):
    headers = ("Name", "Level", "Crime domain")

    def __init__(self, data, parent=None):
        """ data doit être une liste de lignes """
        super().__init__(parent)

        self.rootItem = TreeItem(self.headers)

        self._data = data
        self.setupModelData(self._data, self.rootItem)

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

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
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
            return(QModelIndex())

        return(self.createIndex(parentItem.row(), 0, parentItem))

    def rowCount(self, parent):
        if parent.column() > 0:
            return(0)

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return(parentItem.childCount())

    def setLeader(self, leader):
        self._data = [leader] + self._data[1:]

    def setData(self, index, value, role=Qt.EditRole):
        item = self.getItem(index)
        result = item.setData(index.column(), value)

        return(result)

    def setupModelData(self, lines, parent):
        parents = [parent]
        indentations = [0]

        number = 0

        while number < len(lines):
            position = 0
            while position < len(lines[number]):
                if lines[number][position] != ' ':
                    break
                position += 1

            lineData = lines[number][position:]

            if lineData:
                # Read the column data from the rest of the line.
                columnData = [s for s in lineData if s]

                if position > indentations[-1]:
                    # The last child of the current parent is now the new
                    # parent unless the current parent has no children.

                    if parents[-1].childCount() > 0:
                        parents.append(parents[-1].child(parents[-1]
                                                  .childCount() - 1))
                        indentations.append(position)

                else:
                    while position < indentations[-1] and len(parents) > 0:
                        parents.pop()
                        indentations.pop()

                # Append a new item to the current parent's list of children.
                parents[-1].appendChild(TreeItem(columnData, parents[-1]))

            number += 1


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
