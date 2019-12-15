#!/usr/bin/env python3

import fileinput
from collections import namedtuple, defaultdict
import math

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
      raise Exception("Can't make " + compound)
    recipe = recipes[compound]
    multiple = math.ceil(amount / recipe.output.amount)
    follow(recipe, multiple)

pantry = defaultdict(int, {'FUEL': -1})
cook(pantry, ['ORE'])
print(-pantry['ORE'])
