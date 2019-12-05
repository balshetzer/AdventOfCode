#!/usr/bin/env python3
import fileinput

print(sum(int(line.strip())//3-2 for line in fileinput.input()))