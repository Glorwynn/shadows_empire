#!/usr/bin/python3

import sys

from PySide.QtCore import *
from PySide.QtGui import *

qtApp = QApplication(sys.argv)


class MainWindow(QWidget):
    def __init__(self):
        # Constants statements
        self.WIN_WIDTH = 1280
        self.WIN_HEIGTH = 1024
        self.TABLE_FONT = QFont("Helvetica", 14, QFont.Bold)
        self.turn_number = 1
        self.MAX_TURNS = 10

        # Test variables
        self.leader = "Toto"
        self.team = ["Bob", "Sam", "Tom", "Phil"]

        # Window initialization
        QWidget.__init__(self)
        self.setWindowTitle("Shadows empire")
        self.setMinimumSize(QSize(self.WIN_WIDTH, self.WIN_HEIGTH))

        # Layouts statements
        self.global_layout = QHBoxLayout()
        self.main_layout = QVBoxLayout()
        self.upper_layout = QHBoxLayout()
        self.organisation_layout = QVBoxLayout()
        self.buildings_layout = QVBoxLayout()
        self.lower_layout = QHBoxLayout()
        self.details_layout = QFormLayout()
        self.action_layout = QVBoxLayout()

        # Creating the status zone
        self.status_zone = QTextEdit(self)
        self.status_zone.setReadOnly(True)
        self.status_zone.setMaximumWidth(self.WIN_WIDTH/4)

        # Filling the organisation layout
        self.organisation_tree = QLabel(self.leader)
        self.organisation_tree2 = QLabel(self.team[0])

        self.organisation_layout.addWidget(self.organisation_tree)
        self.organisation_layout.addWidget(self.organisation_tree2)
        self.organisation_layout.addStretch(1)

        # Filling the buildings layout
        self.buildings_tree = QLabel("Repaire")
        self.buildings_tree2 = QLabel("Dortoir")

        self.buildings_layout.addWidget(self.buildings_tree)
        self.buildings_layout.addWidget(self.buildings_tree2)
        self.buildings_layout.addStretch(1)

        # Filling the upper layout
        self.upper_layout.addLayout(self.organisation_layout)
        self.upper_layout.addLayout(self.buildings_layout)

        # Filling the details layout
        self.detail_name_label = QLabel("Name")
        self.detail_name = QLabel(self.leader)
        self.detail_role_label = QLabel("Role")
        self.detail_role = QLabel("Leader")

        self.details_layout.addRow(self.detail_name_label, self.detail_name)
        self.details_layout.addRow(self.detail_role_label, self.detail_role)

        # Filling the action layout
        self.next_turn_btn = QPushButton("Next turn")
        self.next_turn_btn.clicked.connect(self.go)
        self.rename_btn = QPushButton("Rename leader")
        self.rename_btn.clicked.connect(self.rename)

        self.action_layout.addWidget(self.next_turn_btn)
        self.action_layout.addWidget(self.rename_btn)

        # Filling the lower layout
        self.lower_layout.addLayout(self.details_layout)
        self.lower_layout.addLayout(self.action_layout)

        # Filling the main layout
        self.main_layout.addLayout(self.upper_layout)
        self.main_layout.addLayout(self.lower_layout)

        # Filling the global layout
        self.global_layout.addWidget(self.status_zone)
        self.global_layout.addLayout(self.main_layout)
        self.setLayout(self.global_layout)

    @Slot()
    def rename(self):
        self.leader = "Maurice"
        self.detail_name.setText(self.leader)
        self.status_zone.append("The leader is now named {}".format(self.leader))

    @Slot()
    def go(self):
        self.status_zone.append("Turn {} done !".format(self.turn_number))
        self.turn_number += 1

        if self.turn_number >= self.MAX_TURNS:
            pass

    def run(self):
        self.show()
        qtApp.exec_()

app = MainWindow()
app.run()
