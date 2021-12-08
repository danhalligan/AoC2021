# Functions to help read inputs
import re
import os
import requests

def input_str(file):
    return open(file, 'r').read()

def input_lines(file):
    return input_str(file).splitlines()

def input_ints(file):
    txt = input_str(file).rstrip()
    return list(map(int, re.split(r'[\n,]', txt)))

def get_input(day):
    res = requests.get(
        f'https://adventofcode.com/2021/day/{day}/input',
        cookies = {'session': os.environ.get('AOC_SESSION')}
    )
    with open("inputs/day" + f'{day:02d}' + ".txt", 'w') as f:
        f.write(res.text)
