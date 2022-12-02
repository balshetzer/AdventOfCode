#!/usr/bin/env python3

from sys import argv, stdin

f = open(argv[1]) if len(argv) == 2 else stdin

calories = [sum(int(line) for line in elf.split('\n')) for elf in f.read().strip().split('\n\n')]
calories.sort(reverse=True)
print(sum(calories[:3]))
