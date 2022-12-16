# Exceptions
# Import sys to allow exiting program
import sys

# Value error exception
try:
  x = int( input('x: '))
  y = int( input('y: '))
except ValueError:
  print('Error: Invalid input.')
  sys.exit(1)


# Divide by zero by exceptions
try:
  result = x / y
except ZeroDivisionError:
  print('Error: Cannot divide by zero.')
  sys.exit(1)



# Print
print(f'{x} / {y} = {result}')