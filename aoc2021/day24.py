from aoc2021.helpers import *
from collections import deque
import re

def to_value(reg, x):
    if re.match("-*\d+", x): return int(x)
    else: return reg[x]

# Check a given input
def run(program, input):
    reg = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    i = 0
    for line in program:
        inst, *val = line.split()
        if inst == 'inp':
            reg[val[0]] = input[i]
            i += 1
            continue
        a, b = val
        b = to_value(reg, b)
        if inst == 'add':
            reg[a] = reg[a] + b
        elif inst == 'mul':
            reg[a] = reg[a] * b
        elif inst == 'div':
            if to_value(reg, val[1]) == 0:
                print("error")
            else:
                reg[a] = int(reg[a] / b)
        elif inst == 'mod':
            if reg[a] < 0 or b <= 0:
                print("error")
            else:
                reg[a] = reg[a] % b
        elif inst == 'eql':
            reg[a] = 1 if reg[a] == b else 0
    return reg['z']


# Simpler implementation
# def run2(input):
# 	vals = [
# 		[1, 12, 4],
# 		[1, 11, 10],
# 		[1, 14, 12],
# 		[26, -6, 14],
# 		[1, 15, 6],
# 		[1, 12, 16],
# 		[26, -9, 1],
# 		[1, 14, 7],
# 		[1, 14, 8],
# 		[26, -5, 11],
# 		[26, -9, 8],
# 		[26, -5, 3],
# 		[26, -2, 1],
# 		[26, -7, 8]
# 	]
# 	z = 0
# 	for i in range(len(vals)):
# 		w = input[i]
# 		a, b, c = vals[i]
# 		x = int(z % 26 + b != w)
# 		z = z // a * (25 * x + 1) + (w + c) * x
# 	return z

# The above sets up the following conditions:
# x[0]+4-7 == x[13]
# x[1]+10-2 == x[12]
# x[2]+12-6 == x[3]
# x[4]+6-5 == x[11]
# x[5]+16-9 == x[6]
# x[7]+7-9 == x[10]
# x[8]+8-5 == x[9]


def part1(file):
    inc = {0: -3, 1: 8, 2: 6, 4: 1, 5: 7, 7: -2, 8: 3}
    off = {0: 13, 1: 12, 2: 3, 4: 11, 5: 6, 7: 10, 8: 9}

    # biggest value will come from setting lowest x values to high
    x = [None] * 14
    for i in inc.keys():
        for c in range(1, 10):
            if 1 <= c + inc[i] <= 9:
                x[i] = c
                x[off[i]] = c + inc[i]

    program = input_lines(file)
    assert run(program, x) == 0
    return ''.join(map(str, x))

def part2(file):
    inc = {0: -3, 1: 8, 2: 6, 4: 1, 5: 7, 7: -2, 8: 3}
    off = {0: 13, 1: 12, 2: 3, 4: 11, 5: 6, 7: 10, 8: 9}

    x = [None] * 14
    for i in inc.keys():
        for c in range(9, 0, -1):
            if 1 <= c + inc[i] <= 9:
                x[i] = c
                x[off[i]] = c + inc[i]

    program = input_lines(file)
    assert run(program, x) == 0
    return ''.join(map(str, x))

