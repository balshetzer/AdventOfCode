#!/usr/bin/env python3

from parse import compile
from sys import argv, stdin

f = open(argv[1]) if len(argv) == 2 else stdin

pattern = compile('{:d}-{:d},{:d}-{:d}')

def parse(line):
    return pattern.parse(line).fixed

def overlaps(a, b, c, d):
    return a <= c <= b or c <= a <= d

def process(line):
    return overlaps(*parse(line))

print(sum(process(line) for line in f.read().strip().split('\n')))
