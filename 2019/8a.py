#!/usr/bin/env python3
import fileinput

data = [int(i) for i in next(fileinput.input())]

width = 25
height = 6

layer_size = width * height
layers = len(data)//layer_size

def layer(i):
    return data[i*layer_size:(i+1)*layer_size]

def counter(v):
    return lambda i: layer(i).count(v)

zeros = counter(0)
ones = counter(1)
twos = counter(2)

z = min(range(layers), key=zeros)
print(ones(z) * twos(z))
