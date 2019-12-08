#!/usr/bin/env python3
import fileinput
import itertools
import functools

data = [int(i) for i in next(fileinput.input())]

width = 25
height = 6

layer_size = width*height
num_layers = len(data)//layer_size

def chunks(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i+size]

def layers():
    yield from chunks(data, layer_size)

def merge_pixels(top, bottom):
    return bottom if top == 2 else top

def merge_layers(top, bottom):
    return list(itertools.starmap(merge_pixels, zip(top, bottom)))

image = functools.reduce(merge_layers, layers())
for line in chunks(image, width):
    print(''.join('X' if x == 1 else ' ' for x in line))
