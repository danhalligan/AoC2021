from aoc2021.helpers import *
from operator import *
from functools import reduce

def hex2bin(hex):
    bin = format(int(hex, 16), "b")
    return '0' * (4*len(hex) - len(bin)) + bin

class Packet:
    def __init__(self, bin):
        self.bin = bin
        self.version = int(self.popn(3), 2)
        self.type_id = int(self.popn(3), 2)
        self.packets = []
        if self.type_id == 4:
            self.value = ''
            while True:
                v = self.popn(5)
                self.value += v[1:]
                if (v[0] == '0'): break
            self.value = int(self.value, 2)
        else:
            length = {'1': 11, '0': 15}[self.popn(1)]
            if length == 15:
                x = self.popn(int(self.popn(length), 2))
                while len(x):
                    self.packets += [Packet(x)]
                    x = self.packets[-1].bin
            else:
                for i in range(int(self.popn(length), 2)):
                    self.packets += [Packet(self.bin)]
                    self.bin = self.packets[-1].bin

    def popn(self, n):
        val, self.bin = self.bin[:n], self.bin[n:]
        return val

def sum_versions(x):
    return x.version + sum(sum_versions(p) for p in x.packets)

def evaluate(x):
    if x.type_id == 4: return x.value
    vals = [evaluate(p) for p in x.packets]
    fn = [add, mul, min, max, None, gt, lt, eq][x.type_id]
    return reduce(fn, vals)

def part1(file):
    str = input_str(file).rstrip()
    return sum_versions(Packet(hex2bin(str)))

def part2(file):
    str = input_str(file).rstrip()
    return evaluate(Packet(hex2bin(str)))

