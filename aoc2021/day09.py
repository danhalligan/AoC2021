from aoc2021.helpers import *
import numpy as np
from itertools import product

def data(file):
    x = np.array([list(map(int, list(x))) for x in input_lines(file)])
    return np.pad(x, 1, 'maximum')

def neighbours(pos):
    i, j = pos
    return [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]

def array_centre(x):
    rows, cols = np.shape(x)
    return product(range(1, rows-1), range(1, cols-1))

def part1(file):
    x = data(file)
    sum = 0
    for i, j in array_centre(x):
        nbs = [x[nb] for nb in neighbours((i, j))]
        if all(nbs > x[i,j]):
            sum += x[i,j] + 1
    return sum

# flood fill from a given coordinate inside the 2D array
def find_basin(x, i, j):
    basin = set({(i,j)})
    coords = [(i,j)]
    while len(coords) > 0:
        curr = coords.pop()
        coords += [nb for nb in neighbours(curr) if x[nb] < 9 and nb not in basin]
        basin = basin.union(set(coords))
    return basin

def part2(file):
    x = data(file)
    basins = []
    for i, j in array_centre(x):
        if x[i,j] < 9 and not any((i,j) in s for s in basins):
            basins += [find_basin(x, i, j)]
    top = sorted([len(x) for x in basins])[-3:]
    return np.prod(top)
