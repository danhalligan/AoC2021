from aoc2021.helpers import *
import numpy as np
from functools import reduce
from heapq import *

def data(file):
    dat = input_lines(file)
    return np.array([list(map(int, x)) for x in dat])

def neighbours(x, pos):
    i, j = pos
    coords = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [(i, j) for i, j in coords if 0 <= i < x.shape[0] and 0 <= j < x.shape[1]]

def stackr(dat1, dat2):
    return np.concatenate((dat1, dat2), axis = 0)

def stackd(dat1, dat2):
    return np.concatenate((dat1, dat2), axis = 1)

def expand(dat):
    tiles = [(dat+i-1)%9+1 for i in range(1, 5)]
    stacked = reduce(stackr, tiles, dat)
    tiles = [(stacked+i-1)%9+1 for i in range(1, 5)]
    return reduce(stackd, tiles, stacked)

def dijkstra(dat):
    start = (0, 0)
    scores = {start: 0}
    queue = [(0, start)]
    while len(queue) > 0:
        score, pos = heappop(queue)
        for nb in neighbours(dat, pos):
            new = score + dat[nb]
            if new < scores.get(nb, 100000):
                scores[nb] = new
                heappush(queue, (new, nb))
    end = tuple(x-1 for x in dat.shape)
    return scores[end]

def part1(file):
    return dijkstra(data(file))

def part2(file):
    return dijkstra(expand(data(file)))
