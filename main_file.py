from tkinter import *
from table import Table
from player import Player


class Window():

    def __init__(self, master):
        self.master = master
        self.master.geometry('300x100')
        self.master.title('Click and Square')

        self.label1 = Label(self.master, text='Welcome to the Click and Square software', fg='black').pack()
        self.button1 = Button(self.master, text='Start game', bg='white', fg='blue', command=self.start_game).pack()
        self.button2 = Button(self.master, text='Quit game', bg='white', fg='red', command=self.quit_game).pack()

    def start_game(self):
        root2 = Toplevel(self.master)
        table = Table(root2)
        player = Player(table)

    def quit_game(self):
        self.master.destroy()


def main():
    root = Tk()
    my_main_menu = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
