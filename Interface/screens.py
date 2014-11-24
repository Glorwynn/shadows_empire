from tkinter import *
from tkinter import ttk

from consts import*


class StartScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding='3 3 12 12')

        self.grid(column=0, row=0, sticky=(N, W, E, S))

        # Labels
        greetings_lbl = ttk.Label(self, text=MENU_GREETINGS)
        greetings_lbl.grid(column=0, columnspan=3, row=0)

        choice_lbl = ttk.Label(self, text=MENU_CHOICE)
        choice_lbl.grid(column=0, columnspan=3, row=1)

        # Buttons
        new_game_btn = ttk.Button(self, text=MENU_NEW_GAME, command=parent.newGame)
        new_game_btn.grid(column=0, row=2)

        open_game_btn = ttk.Button(self, text=MENU_OPEN_GAME, command=parent.loadGame)
        open_game_btn.grid(column=1, row=2)

        options_btn = ttk.Button(self, text=MENU_OPTIONS, command=parent.getOptions)
        options_btn.grid(column=2, row=2)

        quit_btn = ttk.Button(self, text=MENU_QUIT_APP, command=parent.returnToDsktp)
        quit_btn.grid(column=1, row=3)

        # Final settings
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


class MainScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding='3 3 12 12')

        self.grid(column=0, row=0, sticky=(N, W, E, S))

        name_lbl = ttk.Label(self, text=parent.hero_name)
        name_lbl.grid(column=0, row=0)

        quit_btn = ttk.Button(self, text="Quitter", command=parent.returnToDsktp)
        quit_btn.grid(column=1, row=0)


class OptionScreen(Toplevel):
    def __init__(self, parent, padding='3 3 12 12'):
        super().__init__(parent)
        self.parent = parent

        self.resolutions = StringVar(value=RESOLUTIONS)
        self.resolution = StringVar()

        self.initUI()

    def initUI(self):
        main_frame = ttk.Frame(self)
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.resolutions_box = Listbox(self, listvariable=self.resolutions, height=3)
        self.resolutions_box.grid(column=0, row=0, sticky=W)

        confirm_btn = ttk.Button(self, text="Confirmer", command=self.confirmInfos)
        confirm_btn.grid(column=1, row=0, sticky=W)

    def confirmInfos(self, *args):
        index = int(self.resolutions_box.curselection()[0])
        self.parent.resolution = RESOLUTIONS[index]
        self.parent.initUI()
        self.destroy()


class NewHeroScreen(Toplevel):
    def __init__(self, parent, padding='3 3 12 12'):
        super().__init__(parent)
        self.parent = parent

        self.hero_name = StringVar()

        self.initUI()

    def initUI(self):
        main_frame = ttk.Frame(self)
        main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        greetings_lbl = ttk.Label(self, text=CREATE_GREETINGS)
        greetings_lbl.grid(column=0, columnspan=2, row=0, sticky=W)

        name_lbl = ttk.Label(self, text=CREATE_NAME)
        name_lbl.grid(column=0, row=1, sticky=W)

        name_entry = ttk.Entry(self, textvariable=self.hero_name, width=10)
        name_entry.grid(column=1, row=1, sticky=W)

        confirm_btn = ttk.Button(self, text="Confirmer", command=self.confirmInfos)
        confirm_btn.grid(column=2, row=2, sticky=W)

        name_entry.focus()
        self.bind('<Return>', self.confirmInfos)

    def confirmInfos(self, *args):
        self.parent.hero_name = self.hero_name
        print("Nom du héros : {}".format(self.parent.hero_name.get()))
        self.destroy()

    def getInfos(self):
        return(self.hero_name)
