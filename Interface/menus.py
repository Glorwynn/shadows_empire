from tkinter import *

from consts import *


class FileMenu(Menu):
    def __init__(self, parent, top_parent):
        super().__init__(parent)
        parent.add_cascade(menu=self, label='File')
        self.add_command(label=MENU_NEW_GAME, command=top_parent.newGame)
        self.add_command(label=MENU_OPEN_GAME, command=top_parent.loadGame)
        self.add_command(label=MENU_QUIT_GAME, command=top_parent.quitGame)
        self.add_command(label=MENU_QUIT_APP, command=top_parent.returnToDsktp)


class EditMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)
