from aoc2021.helpers import *

def data():
    return input().splitlines()

def part1():
    x = 0
    y = 0
    for line in data():
        a, b = line.split()
        if a == "forward": x += int(b)
        elif a == "down": y += int(b)
        elif a == "up": y -= int(b)

    return  x*y

def part2():
    x = 0
    y = 0
    aim = 0
    for line in data():
        a, b = line.split()
        if a == "forward":
            x += int(b)
            y += int(b) * -aim
        elif a == "down": aim -= int(b)
        elif a == "up": aim += int(b)

    return  x*y
