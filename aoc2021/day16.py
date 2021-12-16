from aoc2021.helpers import *
from operator import *
from math import prod

def hex2bin(hex):
    map = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    return ''.join(map[x] for x in hex)

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
    vals = [evaluate(p) for p in x.packets]
    if x.type_id == 0:
        return sum(vals)
    elif x.type_id == 1:
        return prod(vals)
    elif x.type_id == 2:
        return min(vals)
    elif x.type_id == 3:
        return max(vals)
    elif x.type_id == 4:
        return x.value
    elif x.type_id == 5:
        return int(gt(*vals))
    elif x.type_id == 6:
        return int(lt(*vals))
    elif x.type_id == 7:
        return int(eq(*vals))

def part1(file):
    str = input_str(file).rstrip()
    x = Packet(hex2bin(str))
    return sum_versions(x)

def part2(file):
    str = input_str(file).rstrip()
    x = Packet(hex2bin(str))
    return evaluate(x)

