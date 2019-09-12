from tkinter import *
import random


class Table:

    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(self.parent, height=400, width=400)
        self.canvas.pack()
        self.darkcolor = {'r': 'darkred', 'g': 'darkgreen', 'b': 'darkblue', 'y': 'darkgoldenrod'}
        self.lightcolor = {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'goldenrod'}
        self.squares = {'r': self.canvas.create_rectangle(0, 0, 200, 200,
                                                          fill='darkred', outline='darkred'),
                        'g': self.canvas.create_rectangle(200, 0, 400, 200,
                                                          fill='darkgreen', outline='darkgreen'),
                        'b': self.canvas.create_rectangle(0, 200, 200, 400,
                                                          fill='darkblue', outline='darkblue'),
                        'y': self.canvas.create_rectangle(200, 200, 400, 400,
                                                          fill='darkgoldenrod', outline='darkgoldenrod')}

        self.status = Label(self.parent, text='Good luck!')
        self.status.pack(side=BOTTOM, fill=X)
