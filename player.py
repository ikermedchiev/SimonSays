from tkinter import *
import random
from table import Table


class Player:

    def __init__(self, table):
        self.table = table
        self.high_score = 0
        self.table.parent.bind('<h>', self.score)
        self.index = {v: k for k, v in self.table.squares.items()}
        self.draw_table()

    def draw_table(self):
        self.pattern = random.choice('rgby')
        self.selections = ''
        self.table.parent.after(500, self.animate)

    def animate(self, idx=0):
        c = self.pattern[idx]
        self.table.canvas.itemconfig(self.table.squares[c], fill=self.table.lightcolor[c],
                                     outline=self.table.lightcolor[c])
        self.table.parent.after(250, lambda: self.table.canvas.itemconfig(self.table.squares[c],
                                                                          fill=self.table.darkcolor[c],
                                                                          outline=self.table.darkcolor[c]))

        idx += 1
        if idx < len(self.pattern):
            self.table.parent.after(500, lambda: self.animate(idx))
        else:
            self.table.canvas.bind('<1>', self.select)

    def select(self, event=None):
        id = self.table.canvas.find_withtag("current")[0]
        color = self.index[id]
        self.selections += color
        self.table.canvas.itemconfig(id,
                                     fill=self.table.lightcolor[color], outline=self.table.lightcolor[color])
        self.table.parent.after(400, lambda: self.table.canvas.itemconfig(id,
                                                                          fill=self.table.darkcolor[color],
                                                                          outline=self.table.darkcolor[color]))
        if self.pattern == self.selections:
            self.table.canvas.unbind('<1>')
            self.table.status.config(text='Correct!')
            self.table.parent.after(500, lambda: self.table.status.config(text=''))
            self.pattern += random.choice('rgby')
            self.selections = ''
            self.high_score = len(self.pattern) - 1
            self.table.parent.after(1000, self.animate)

        elif self.pattern[len(self.selections) - 1] != color:
            self.table.canvas.unbind('<1>')
            self.table.status.config(text='Wrong!')
            self.high_score = 0
            self.table.parent.after(500, lambda: self.table.status.config(text=''))
            self.table.parent.after(1000, self.draw_table)

    def score(self, event=None):
        self.table.status.config(text=self.high_score)
        self.table.parent.after(1000, lambda: self.table.status.config(text=''))


def main():
    root = Tk()
    table = Table(root)
    player = Player(table)
    root.mainloop()

if __name__ == '__main__':
    main()
