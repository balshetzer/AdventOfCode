#!/usr/bin/env python3

import fileinput

grid = {(x,y): int(digit) for y, line in enumerate(fileinput.input()) for x, digit in enumerate(line.strip())}
dirs = ((-1, 0), (1,0), (0, -1), (0, 1))
neighbors = lambda p: tuple(filter(lambda p: p in grid, ((p[0]+dx, p[1]+dy) for dx,dy in dirs)))
low = lambda p: all(grid[p] < grid[n] for n in neighbors(p))
risk = sum(1 + grid[p] for p in grid if low(p))
print(risk)