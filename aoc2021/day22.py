from aoc2021.helpers import *
import re
from collections import defaultdict
import numpy as np

def data(file):
    s = input_str(file).splitlines()
    for line in s:
        parts = line.split()
        d = re.findall("-*\d+", parts[1])
        d = list(map(int, d))
        yield [
            parts[0] == "on",
            ((d[0], d[1]), (d[2], d[3]), (d[4], d[5]))
        ]

def part1(file):
    dat = list(data(file))
    space = defaultdict(lambda: False)
    for on, coord in dat:
        if all(x[0] >= -50 and x[1] <= 50 for x in coord):
            for x in range(coord[0][0], coord[0][1]+1):
                for y in range(coord[1][0], coord[1][1]+1):
                    for z in range(coord[2][0], coord[2][1]+1):
                        space[(x,y,z)] = on
    return sum(space.values())

def volume(x, y, z):
    return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)

def overlapping(a, b):
    (x, X), (y, Y), (z, Z) = a
    (u, U), (v, V), (w, W) = b
    return not (x > U or X < u or y > V or Y < v or z > W or Z < w)

def subcubes(a, b):
    (x, X), (y, Y), (z, Z) = a
    (u, U), (v, V), (w, W) = b
    if not overlapping(a, b):
        yield b
    else:
        if x > u:
            yield ((u, x - 1), (v, V), (w, W))
        if X < U:
            yield ((X + 1, U), (v, V), (w, W))
        if y > v:
            yield ((max(u, x), min(U, X)), (v, y - 1), (w, W))
        if Y < V:
            yield ((max(u, x), min(U, X)), (Y + 1, V), (w, W))
        if z > w:
            yield ((max(u, x), min(U, X)), (max(v, y), min(V, Y)), (w, z - 1))
        if Z < W:
            yield ((max(u, x), min(U, X)), (max(v, y), min(V, Y)), (Z + 1, W))

def part2(file):
    dat = list(data(file))
    cubes = []
    for state, c1 in dat:
        new = []
        for c2 in cubes:
            for subcube in subcubes(c1, c2):
                new.append(subcube)
        if state:
            new.append(c1)
        cubes = new
    return sum(volume(*cube) for cube in cubes)
