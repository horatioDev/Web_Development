# To use square function import from functions.py file

# The whole module which requires dot.notation for accessing the square function
import functions

# Just the square function
from functions import square



# Loop through a range that returns its value squared every iteration
for i in range(10):
  # w/ dot.notation
  print(f'The square  of {i} is {functions.square(i)}')
  # print(f'The square  of {i} is {square(i)}')
