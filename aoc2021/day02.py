from aoc2021.helpers import *

def part1():
    x, y = 0, 0
    for line in input_lines(2):
        a, b = line.split()
        if a == "forward": x += int(b)
        elif a == "down": y += int(b)
        elif a == "up": y -= int(b)

    return  x*y

def part2():
    x, y, aim = 0, 0, 0
    for line in input_lines(2):
        a, b = line.split()
        if a == "forward":
            x += int(b)
            y += int(b) * -aim
        elif a == "down": aim -= int(b)
        elif a == "up": aim += int(b)

    return  x*y
