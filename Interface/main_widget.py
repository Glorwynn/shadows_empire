from models import *
from details_box import *


class MainWidget(QWidget):
    def __init__(self, parent):
        # Constants
        self.MAX_TURNS = 10
        self.turn_number = 1

        # Test variables
        self.leader = ("Splinter", "10", "Génie du mal")
        self.team = [self.leader,
                     (" ", "Michelangelo", "2", "Vol"),
                     (" ", "Rafaelo", "1", "Assassinat"),
                     (" ", "Leonardo", "6", "Prostitution"),
                     (" ", "Donatello", "4", "Contrebande")]
        self.lair = "Grande cave dans le ghetto orc"
        self.lair_compo = ["Dortoir (4 places)", "Chambre du maître",
                           "Terrain d'entraînement Ninju-Tsu", "Four à pizzas"]

        # Widget initialization
        QWidget.__init__(self)
        self.parent = parent

        # Interface construction
        self.initUI()

    def initUI(self):
        # Layouts statements
        self.global_layout = QVBoxLayout()
        self.infos_layout = QVBoxLayout()
        self.upper_layout = QHBoxLayout()
        self.organisation_layout = QVBoxLayout()
        self.buildings_layout = QVBoxLayout()
        self.action_layout = QHBoxLayout()
        self.btn_layout = QGridLayout()

        # Creating the status zone
        self.status_zone = QTextEdit(self)
        self.status_zone.setReadOnly(True)
        self.status_zone.setMaximumSize(self.parent.WIN_WIDTH/1.5,
                                        self.parent.WIN_HEIGTH/10)

        # Creating the details zone
        self.details_box = DetailsBox(self, "Details")

        # Filling the organisation layout
        self.organisation_tree_model = OrganizationTreeModel(self.team)
        self.organisation_tree_view = QTreeView()
        self.organisation_tree_view.clicked.connect(self.details_box.display)
        self.organisation_tree_view.setModel(self.organisation_tree_model)
        self.organisation_layout.addWidget(self.organisation_tree_view)
        self.organisation_layout.addStretch(1)

        # Filling the buildings layout
        self.buildings_tree = BuildingsTree(self, self.lair, self.lair_compo)
        self.buildings_layout.addWidget(self.buildings_tree)
        self.buildings_layout.addStretch(1)

        # Filling the upper layout
        self.upper_layout.addLayout(self.organisation_layout)
        self.upper_layout.addLayout(self.buildings_layout)

        # Filling the buttons layout
        self.rename_btn = QPushButton("Rename leader")
        self.rename_btn.clicked.connect(self.rename)
        self.next_turn_btn = QPushButton("Next turn")
        self.next_turn_btn.clicked.connect(self.go)

        self.btn_layout.addWidget(self.rename_btn, 0, 0)
        self.btn_layout.addWidget(self.next_turn_btn, 1, 0, 1, 2)

        # Filling the main layout
        self.infos_layout.addLayout(self.upper_layout)
        self.infos_layout.addWidget(self.details_box)

        # Filling the action layout
        self.action_layout.addWidget(self.status_zone)
        self.action_layout.addLayout(self.btn_layout)

        # Filling the global layout
        self.global_layout.addLayout(self.infos_layout)
        self.infos_layout.addLayout(self.action_layout)

        self.setLayout(self.global_layout)

    @Slot()
    def rename(self):
        self.leader = self.renameDialog()
        self.details_box.name.setText(self.leader)
        self.organisation_tree_model.setLeader(("Ben", "1", "Petite frappe"))
        self.status_zone.append("The leader is now {}.".format(self.leader))

    @Slot()
    def go(self):
        self.status_zone.append("Turn {} done !".format(self.turn_number))
        self.turn_number += 1

        if self.turn_number >= self.MAX_TURNS:
            pass

    def renameDialog(self):
        nv_nom, ok = QInputDialog.getText(self, 'Renommer un personnage',
                                          'Entrez le nouveau nom :')
        return(nv_nom)
