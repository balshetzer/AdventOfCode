import more_itertools

C = '''
 ## 
#  #
#   
#   
#  #
 ## 
'''.strip('\n')

E = '''
####
#   
### 
#   
#   
####
'''.strip('\n')

H = '''
#  #
#  #
####
#  #
#  #
#  #
'''.strip('\n')

J = '''
  ##
   #
   #
   #
#  #
 ## 
'''.strip('\n')

L = '''
#   
#   
#   
#   
#   
####
'''.strip('\n')

letters = {C: 'C', E: 'E', H: 'H', J: 'J', L: 'L'}

def ocr(image):
  lines = image.split('\n')
  chunked = [[line[i:i+4] for i in range(0, len(line), 5)] for line in lines]
  letter_images = ['\n'.join(letter_lines) for letter_lines in zip(*chunked)]
  return ''.join(letters[letter_image] for letter_image in letter_images)
