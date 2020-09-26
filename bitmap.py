import os
from collections import namedtuple
from copy import copy

def clear():
    os.system("clear")

class Bitmap():
    def __init__(self, width = 40, height = 40, char='@'):
        assert width > 0 and height > 0
        self.width = width
        self.height = height
        self.char = char
        self.map = [[False for w in range(width)] for h in range(height)]


    def chardisplay(self):
        txt = [''.join(' ' if not bit else self.char
                       for bit in row)
               for row in self.map]
        # Boxing
        txt = ['|'+row+'|' for row in txt]
        txt.insert(0, '+' + '-' * self.width + '+')
        txt.append('+' + '-' * self.width + '+')
        #print('\n'.join(reversed(txt)))
        return '\n'.join(txt)

    def animate(self, x):
        try:
            while True:
                clear()
                x()
                print("{}".format(self.chardisplay()))
        except KeyboardInterrupt:
            print("\nclosing animation....")

    def set(self, x, y):
        self.map[y][x] = True

    def remove(self, x, y):
        self.map[y][x] = False

    def get(self, x, y):
        return self.map[y][x]
 
    def get_char(self, x, y):
        return self.char if self.map[y][x] else ' '

