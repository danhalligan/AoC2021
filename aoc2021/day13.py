from aoc2021.helpers import *
import numpy as np

def data(file):
    dots, folds = input_str(file).rstrip().split("\n\n")
    dots = [list(map(int, x.split(','))) for x in dots.split("\n")]
    folds = [x.split('=') for x in folds.split('\n')]
    for f in folds:
        f[0] = f[0][-1]
        f[1] = int(f[1])
    return dots, folds

def paper(dots):
    size = (max(x[0] for x in dots)+1, max(x[1] for x in dots)+1)
    x = np.zeros(size)
    for i, j in dots:
        x[i,j] = 1
    return x

def fold(x, i, axis):
    if axis == 'x':
        x1 = x[0:i, ]
        x2 = np.flip(x[(i+1):, ], 0)
    else:
        x1 = x[:,0:i]
        x2 = np.flip(x[:, (i+1):], 1)
    return np.add(x1, x2)

def part1(file):
    dots, folds = data(file)
    x = paper(dots)
    x = fold(x, folds[0][1], folds[0][0])
    return sum(sum(x >= 1))

def part2(file):
    dots, folds = data(file)
    x = paper(dots)
    for (axis, pos) in folds:
        x = fold(x, pos, axis)
    x = np.rot90(np.flip(x > 1, 1))
    for r in x:
        print(''.join({False:' ', True:'█'}[i] for i in r))
