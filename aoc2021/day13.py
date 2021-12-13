from aoc2021.helpers import *
import numpy as np
from functools import reduce

def data(file):
    dots, folds = input_str(file).rstrip().split("\n\n")
    dots = [list(map(int, x.split(','))) for x in dots.split("\n")]
    folds = [x.split('=') for x in folds.split('\n')]
    for f in folds:
        f[0] = f[0][-1]
        f[1] = int(f[1])
    return dots, folds

def paper(dots):
    size = (max(x[1] for x in dots)+1, max(x[0] for x in dots)+1)
    x = np.zeros(size)
    for i, j in dots: x[j, i] = 1
    return x

def fold(x, loc):
    axis, i = loc
    if axis == 'y':
        return x[:i, :] + np.flip(x[i+1:, :], axis = 0)
    if axis == 'x':
        return x[:, :i] + np.flip(x[:, i+1:], axis = 1)

def part1(file):
    dots, folds = data(file)
    x = paper(dots)
    x = fold(x, folds[0])
    return sum(sum(x >= 1))

def part2(file):
    dots, folds = data(file)
    x = reduce(fold, folds, paper(dots)) >= 1
    x = [''.join({False:' ', True:'█'}[i] for i in r) for r in x]
    return "\n\n" + "\n".join(x)
