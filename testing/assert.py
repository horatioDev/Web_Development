# Assert

# Import math for use in optimization
import math


def square(n):
  return n * n


# assert square(10) == 100 # Ignores if true
# assert square(5) == 26 # AssertionError

# print(square(10) == 100)
# print(square(5) == 26)

def is_prime(n):
  # Check if n is less than 2, then n is not a prime number
  if n < 2:
    return False
  
  # Loop through n, check if n is divisible by itself and equal 0, then n is not a prime number
  # for i in range(2, n):
  
  # Optimization
  for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
      return False

  return True

print(is_prime(0)) # False
print(is_prime(1)) # False
print(is_prime(5)) # True