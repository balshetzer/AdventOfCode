#!/usr/bin/env python3

import string

A='''\
 ##  
#  # 
#  # 
#### 
#  # 
#  # '''

B = '''\
### 
#  #
### 
#  #
#  #
### '''

C = '''\
 ## 
#  #
#   
#   
#  #
 ## '''

E = '''\
####
#
### 
#   
#   
####'''

F = '''\
####
#
###
#
#
#'''

G = '''\
 ## 
#  #
#   
# ##
#  #
 ###'''

H = '''\
#  #
#  #
####
#  #
#  #
#  #'''

J = '''\
  ##
   #
   #
   #
#  #
 ## '''

K = '''\
#  #
# # 
##  
# # 
# # 
#  #'''

L = '''\
#   
#   
#   
#   
#   
####'''

P = '''\
### 
#  #
#  #
### 
#   
#   '''

R = '''\
### 
#  #
#  #
### 
# # 
#  #'''

U = '''\
#  #
#  #
#  #
#  #
#  #
 ## '''

Y = '''\
#   #
#   #
 # # 
  #  
  #  
  # '''

Z = '''\
####
   #
  # 
 #  
#   
####'''

def pad(image):
  return '\n'.join(line + ' ' * (5-len(line)) for line in image.split('\n'))

map_text_to_image = {letter: pad(globals()[letter]) for letter in string.ascii_uppercase if letter in globals()}
map_image_to_text = {image: text for text, image in map_text_to_image.items()}

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

def text_to_image(s):
  for i, letter in enumerate(s):
    if letter not in map_text_to_image:
      print('Unknown', ordinal(i+1), 'letter:', letter)
  images = [map_text_to_image[letter] for letter in s if letter in map_text_to_image]
  lines = [''.join(line) for line in zip(*[image.split('\n') for image in images])]
  return '\n'.join(lines)

def image_to_text(image):
  lines = [''.join('#' if x != ' ' else ' ' for x in line) for line in image.split('\n')]
  chunked = [[line[i:i+5] for i in range(0, len(line), 5)] for line in lines]
  images = [pad('\n'.join(letter_lines)) for letter_lines in zip(*chunked)]
  for i, image in enumerate(images):
    if image not in map_image_to_text:
      print('Unknown', ordinal(i+1), 'letter:')
      print(image)
  return ''.join(map_image_to_text[image] for image in images if image in map_image_to_text)

if __name__ == '__main__':
  import fileinput
  try:
    lines = fileinput.input()
    while (line := next(lines).strip('\n')):
      if line.isalpha():
        image = text_to_image(line)
        print(image)
        print(image_to_text(image))
      else:
        input = [line]
        for i in range(5):
          input.append(next(lines).strip('\n'))
        image = '\n'.join(input)
        text = image_to_text(image)
        print(text)
        print(text_to_image(text))
  except StopIteration:
    pass