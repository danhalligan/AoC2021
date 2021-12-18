from aoc2021.helpers import *
import re
from math import floor, ceil
from functools import reduce

def ispair(x):
    return bool(re.match("\d+,\d+", ''.join(x)))

def addstr(a, b):
    return str(int(a) + int(b))

def addprev(x, i):
    j = i - 1
    while j > 0:
        if x[j].isdigit():
            x[j] = addstr(x[j], x[i])
            return
        j -= 1

def addnext(x, i):
    j = i + 1
    while j < len(x):
        if x[j].isdigit():
            x[j] = addstr(x[j], x[i])
            return
        j += 1

def explode(x):
    counter = 0
    for i in range(len(x)):
        if x[i] == '[':
            counter += 1
        elif x[i] == ']':
            counter -= 1
        if ispair(x[i:i+3]) and counter > 4:
            j = addprev(x, i)
            j = addnext(x, i+2)
            x = x[:i-1] + ['0'] + x[i+4:]
            return True, x
    return False, x

def split(x):
    for i in range(len(x)):
        if re.match('\d\d', x[i]):
            v = int(x[i])
            x = x[:i] + add([str(floor(v/2))], [str(ceil(v/2))]) + x[i+1:]
            return True, x
    return False, x

def add(a, b):
    return ['['] + a + [','] + b + [']']

def process(a, b):
    x = add(list(a), list(b))
    changed = True
    while changed:
        changed, x = explode(x)
        if not changed: changed, x = split(x)
    return x

def magnitude(x):
    while len(x) > 1:
        for i in range(len(x)):
            if ispair(x[i:i+3]):
                x = x[:i-1] + [str(int(x[i])*3 + int(x[i+2])*2)] + x[i+4:]
    return int(x[0])

def part1(file):
    dat = input_lines("inputs/day18.txt")
    tot = reduce(process, dat)
    return magnitude(tot)

def part2(file):
    dat = input_lines("inputs/day18.txt")
    best = 0
    for i in range(len(dat)):
        for j in range(len(dat)):
            if i == j: continue
            best = max(best, magnitude(process(dat[i], dat[j])))
    return best
