#!/usr/bin/env python3

import fileinput
from collections import namedtuple, deque, defaultdict
import math
import bisect

Ingredient = namedtuple('Ingredient', ['amount', 'compound'])
Recipe = namedtuple('Recipe', ['inputs', 'output'])

def parse_ingredient(s):
  a, c = s.split(' ')
  return Ingredient(int(a), c)

def parse_recipe(s):
  inputs, output = s.strip().split(' => ')
  return Recipe(tuple(map(parse_ingredient, inputs.split(', '))), 
                parse_ingredient(output))

recipes = {recipe.output.compound: recipe for recipe in map(parse_recipe, fileinput.input())}
intermediates = set(r.output.compound for r in recipes.values() if r.output.compound != 'FUEL')

def cook(pantry, track=set()):
  def follow(recipe, multiple):
    for i in recipe.inputs:
      pantry[i.compound] -= multiple * i.amount
    pantry[recipe.output.compound] += multiple * recipe.output.amount

  def need():
    while True:
      l = [(compound, -amount) for compound, amount in pantry.items() if compound not in track and amount < 0]
      if not l:
        return
      for i in l:
        yield i

  for compound, amount in need():
    if compound not in recipes:
      return False
    recipe = recipes[compound]
    multiple = math.ceil(amount / recipe.output.amount)
    follow(recipe, multiple)
  return True

class OreForFuel:
  def __init__(self, size):
    self._size = size
    
  def __len__(self):
    return self._size
    
  def __getitem__(self, amount):
    pantry = defaultdict(int, {'FUEL': -amount})
    if not cook(pantry, ['ORE']):
      print("failed to make fuel")
    return -pantry['ORE']

print(bisect.bisect_left(OreForFuel(1000000000000), 1000000000000)-1)
