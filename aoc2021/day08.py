from aoc2021.helpers import *
from collections import Counter
import numpy as np

# mapping from digit to segment
info = [
    [['a','b','c','e','f','g'],  '0'],
    [['c','f'],  '1'],
    [['a','c','d','e','g'],  '2'],
    [['a','c','d','f','g'],  '3'],
    [['b','c','d','f'],  '4'],
    [['a','b','d','f','g'],  '5'],
    [['a','b','d','e','f','g'],  '6'],
    [['a','c','f'],  '7'],
    [['a','b','c','d','e','f','g'],  '8'],
    [['a','b','c','d','f','g'],  '9']
]

# Each digit has a unique value based on the sum of the frequency of the
# the signals. For example, c occurs 8 and f occurs 9 times above, so the
# digit 1 can be represented as 8 + 9 = 17 (which is unique)

# First create a map from unqiue sum to digit
counts = Counter(np.concatenate([x[0] for x in info]))
lookup = dict([sum(counts[y] for y in x[0]), x[1]] for x in info)

# To decode, we use hash lookup from the unique sums
def decode(line, lookup):
    wires, digits = line.split(" | ")
    wires = wires.split()
    wires = [sorted(list(x)) for x in wires]

    digits = digits.split()
    digits = [''.join(sorted(list(x))) for x in digits]

    count = Counter(np.concatenate(wires))
    map = dict([''.join(x), lookup[sum(count[y] for y in x)]] for x in wires)
    return [int(map[digit]) for digit in digits]

# part 1
def part1(file = input_file(8)):
    dat = input_lines(file)
    res = [decode(line, lookup) for line in dat]
    counts = Counter(np.concatenate(res))
    return counts[1] + counts[4] + counts[7] + counts[8]

# part 2
def part2(file = input_file(8)):
    dat = input_lines(file)
    res = [decode(line, lookup) for line in dat]
    return sum(int(''.join([str(y) for y in x])) for x in res)
