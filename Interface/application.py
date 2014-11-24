from tkinter import *

from consts import *
from menus import *
from screens import *


class MainWindow(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.option_add('*tearOff', FALSE)

        self.initVariables()
        self.initUI()
        StartScreen(self)

    def initUI(self):
        # Screen resolution
        self.geometry(self.resolution)

        # Menus
        menu_bar = Menu(self)
        self['menu'] = menu_bar
        FileMenu(menu_bar, self)
        EditMenu(menu_bar)

    def initVariables(self):
        # Graphical variables
        self.resolution = STD_RESOLUTION

        # Game variables
        self.hero_name = StringVar()

    def newGame(self):
        NewHeroScreen(self)
        MainScreen(self)

    def loadGame(self):
        pass

    def getOptions(self):
        OptionScreen(self)

    def quitGame(self):
        self.initUI()

    def returnToDsktp(self):
        self.destroy()

root = MainWindow("Shadows Empire")
root.mainloop()
