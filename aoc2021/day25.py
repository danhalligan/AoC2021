from aoc2021.helpers import *
import numpy as np

def data(file):
    dat = open(file).read().splitlines()
    return np.array([list(x) for x in dat])

def move(x, f, t):
    v = x[t] == '.'
    x[(t[0][v], t[1][v])] = x[(f[0][v], f[1][v])]
    x[(f[0][v], f[1][v])] = '.'
    return sum(v)

def move_east(x):
    east = np.where(x == ">")
    nbs = (east[0], (east[1] + 1) % x.shape[1])
    return move(x, east, nbs)

def move_south(x):
    south = np.where(x == "v")
    nbs = ((south[0] + 1) % x.shape[0], south[1])
    return move(x, south, nbs)

def part1(file):
    x = data(file)
    count = 0
    while move_east(x) + move_south(x) > 0:
        count += 1
    return count + 1
