#!/usr/bin/env python3

import fileinput
from collections import namedtuple, deque, defaultdict
from math import ceil

def lcm(*nums):
  return reduce(lambda a, b: a * b // gcd(a, b), nums)

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

ore = 0
want = deque([Ingredient(1, 'FUEL')])
have = defaultdict(int)

while want:
  cur = want.pop()
  print("We want:", cur)
  if cur.compound == 'ORE':
    ore += cur.amount
    print("We get it all from the mines!")
    continue
  if (reserve := have[cur.compound]) > 0:
    print("We have", reserve, "in reserve")
    if reserve >= cur.amount:
      have[cur.compound] -= cur.amount
      print("We take", reserve, "and leave", have[cur.compound], "in the store")
    else:
      have[cur.compound] -= reserve
      want.append(Ingredient(cur.amount-reserve, cur.compound))
      print("We take", reserve, "and still need", cur.amount-reserve)
    continue
  recipe = recipes[cur.compound]
  multiple = ceil(cur.amount / recipe.output.amount)
  print("We'll make it with", multiple, "times", recipe)
  print("We'll need", multiple * recipe.inputs)
  want.extend(recipe.inputs * multiple)
  have[recipe.output.compound] += multiple * recipe.output.amount - cur.amount
  print("And make an extra", multiple * recipe.output.amount - cur.amount, cur.compound)

print(ore)