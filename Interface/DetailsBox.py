from PySide.QtCore import *
from PySide.QtGui import *


class DetailsBox(QGroupBox):
    def __init__(self, parent, name):
        QGroupBox.__init__(self, name)
        self.parent = parent

        self.initUI()

    def initUI(self):
        self.details_layout = QFormLayout()

        self.name_label = QLabel("Name")
        self.lvl_label = QLabel("Level")
        self.role_label = QLabel("Crime domain")

        self.name = QLabel()
        self.lvl = QLabel()
        self.role = QLabel()

        self.details_layout.addRow(self.name_label, self.name)
        self.details_layout.addRow(self.lvl_label, self.lvl)
        self.details_layout.addRow(self.role_label, self.role)

        self.setLayout(self.details_layout)

    @Slot(QTreeWidgetItem, int)
    def display(self, item, col):
        self.name.setText(item.text(0))
        self.lvl.setText(item.text(1))
        self.role.setText(item.text(2))
