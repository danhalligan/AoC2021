from aoc2021.helpers import *
import numpy as np

def data(file):
    return np.array([list(map(int, list(x))) for x in input_lines(file)])

def neighbours(pos):
    i, j = pos
    return [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]

def part1(file):
    dat = np.pad(data(file), 1, 'maximum')
    sum = 0
    for i in range(1, np.shape(dat)[0]-1):
        for j in range(1, np.shape(dat)[1]-1):
            nbs = [dat[x] for x in neighbours((i, j))]
            if all(nbs > dat[i,j]):
                sum += dat[i,j] + 1
    return sum

def find_basin(dat, i, j):
    basin = set({(i,j)})
    nbs = [(i,j)]
    while len(nbs) > 0:
        curr = nbs.pop()
        nbs += [x for x in neighbours(curr) if dat[x] < 9 and x not in basin]
        basin = basin.union(set(nbs))
    return basin

def part2(file):
    dat = np.pad(data(file), 1, 'maximum')
    basins = []
    for i in range(1, np.shape(dat)[0]-1):
        for j in range(1, np.shape(dat)[1]-1):
            if dat[i,j] < 9:
                if any((i,j) in s for s in basins):
                    continue
                basins += [find_basin(dat, i, j)]

    top = sorted([len(x) for x in basins])[-3:]
    return np.prod(top)
