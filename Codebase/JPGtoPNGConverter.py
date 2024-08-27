import sys
import os
from PIL import Image, ImageFilter

# Grab first and second argument, # PokeDex / new folder

# Check if new / exists, if not create it.

# loop through Pokedex,
# Convert images to png
# Save to new folder

#arg1 = sys.argv[1]
#arg2 = sys.argv[2]

#print(f"Argument 1: {arg1}")
#print(f"Argument 2: {arg2}")

# Coding Stuff
# Testing Images

import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)
    

for filename in os.listdir(path):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f'{path}{filename}')
  #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
  img.save(f'{directory}/{clean_name}.png', 'png')
  print('all done!')