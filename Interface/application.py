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

    def initUI(self):
        # Menus
        menu_bar = Menu(self)
        self['menu'] = menu_bar
        FileMenu(menu_bar, self)
        EditMenu(menu_bar)

        # Main frame
        SplashScreen(self)

    def initVariables(self):
        self.hero_name = StringVar()

    def newGame(self):
        NewHeroScreen(self)
        MainScreen(self)

    def loadGame(self):
        pass

    def quitGame(self):
        self.initUI()

    def returnToDsktp(self):
        self.destroy()

root = MainWindow("Shadows Empire")
root.mainloop()
