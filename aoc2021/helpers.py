# Functions to help read inputs
import re
import os

def input_file(day):
    file = "inputs/day" + f'{day:02d}' + ".txt"
    if 'PYTEST' in os.environ: file = "tests/" + file
    return file

def input_str(day):
    return open(input_file(day), 'r').read()

def input_lines(day):
    return input_str(day).splitlines()

def input_ints(day):
    txt = input_str(day).rstrip()
    return list(map(int, re.split(r'[\n,]', txt)))
