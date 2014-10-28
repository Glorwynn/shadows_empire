from PySide.QtCore import *
from PySide.QtGui import *


class DetailsBox(QGroupBox):
    def __init__(self, parent, name):
        QGroupBox.__init__(self, name)
        self.parent = parent

        self.initUI()

    def initUI(self):
        self.details_layout = QFormLayout()

        self.detail_name_label = QLabel("Name")
        self.detail_name = QLabel(self.parent.leader)
        self.detail_role_label = QLabel("Role")
        self.detail_role = QLabel("Leader")

        self.details_layout.addRow(self.detail_name_label, self.detail_name)
        self.details_layout.addRow(self.detail_role_label, self.detail_role)

        self.setLayout(self.details_layout)

    @Slot()
    def display(self):
        self.detail_name.setText("Bla")
        self.detail_role_label.setText("Blo")
