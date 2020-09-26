import argparse
import random
import os
import time

from bitmap import Bitmap


def clear():
    os.system("clear")

ap = argparse.ArgumentParser()

ap.add_argument("--height", type=int, required=False, help="Height of the canvas")
ap.add_argument("--width", type=int, required=False, help="Width of the Canvas")
ap.add_argument("--char",  type=str, required=False, help="character of cell(default='@')")
ap.add_argument("--ratio", type=float, required=False, help="probability of population in initial population")

args = ap.parse_args()
width = args.width or 45
height = args.height or 20
char = args.char or '@'
ratio = args.ratio or 0.85


cells = Bitmap(width, height, char=char)

def random_cells():
    for i in range(width):
        for j in range(height):
            if(random.random() > ratio):
                cells.set(i, j)

def glider():
    cells.set(1, 1)
    cells.set(2, 2)
    cells.set(3, 2)
    cells.set(2, 3)
    cells.set(1, 3)

def count_neigh(x, y, new_map):
    c = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            #print(x+i, y+j, end="")
            #print(cells.get(x+i, y+j))
            if i == x and j == y:
                continue
            val = new_map[y+j][x+i]
            if(val == '@'):
                c.append(1)
    return sum(c)


# Initializing population
random_cells()

try:
    while True:
        new_map = [[False for i in range(width)] for j in range(height)]
        cmap = cells.map
        time.sleep(0.1)
        clear()
        print(cells.chardisplay())

        for i in range(1, width - 1):
            for j in range(1, height - 1):

                c = cmap[j-1][i-1] + cmap[j-1][i] + cmap[j-1][i+1]+ cmap[j][i-1]+ cmap[j][i+1]+ cmap[j+1][i-1]+ cmap[j+1][i] + cmap[j+1][i+1]
                if (not cmap[j][i] and c == 3):
                    new_map[j][i] = True

                if (cmap[j][i]  and c in (2, 3)):
                    new_map[j][i] = True

                if (cmap[j][i] and c < 2):
                    new_map[j][i] = False

        cells.map = new_map

except KeyboardInterrupt:
    print("\nClosing animation")
