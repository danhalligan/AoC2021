# Functions to help read inputs
import re
import os

def input_file(day):
    file = "inputs/day" + f'{day:02d}' + ".txt"
    if 'PYTEST' in os.environ: file = "tests/" + file
    return file

def input_str(file):
    return open(file, 'r').read()

def input_lines(file):
    return input_str(file).splitlines()

def input_ints(file):
    txt = input_str(file).rstrip()
    return list(map(int, re.split(r'[\n,]', txt)))
