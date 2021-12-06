# Functions to help read inputs
import re

def input_str(day):
    return open("inputs/day" + f'{day:02d}' + ".txt", 'r').read()

def input_lines(day):
    return input_str(day).splitlines()

def input_ints(day):
    txt = input_str(day).rstrip()
    return list(map(int, re.split(r'[\n,]', txt)))
