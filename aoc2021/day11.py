from aoc2021.helpers import *
import numpy as np

def data(file):
    return np.array([list(map(int, list(x))) for x in input_lines(file)])

# neighbours of a position as array of rows and array of columns suitable
# for direct indexing in numpy array
def neighbours(x, pos):
    i, j = pos
    r = np.array([i-1, i-1, i-1, i, i, i+1, i+1, i+1])
    c = np.array([j-1, j, j+1, j-1, j+1, j-1, j, j+1])
    w = np.where((r >= 0) & (r < x.shape[0]) & (c >= 0) & (c < x.shape[1]))
    return r[w], c[w]

# list of coordinates as tuples that are about to flash
def will_flash(x):
    return list(zip(*np.where(x > 9)))

def step(x):
    x += 1
    flashed = set()
    toflash = will_flash(x)
    while len(toflash) > 0:
        for pos in toflash: x[neighbours(x, pos)] += 1
        flashed = flashed.union(toflash)
        toflash = set(will_flash(x)) - flashed
    for p in flashed: x[p] = 0
    return np.sum(x == 0)

def part1(file):
    x = data(file)
    return sum(step(x) for _ in range(100))

def part2(file):
    x = data(file)
    for i in range(1000):
        if step(x) == 100: return i+1
