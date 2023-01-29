# Is Prime ?

# Import math for use in optimization
import math


def is_prime(n):
  # Check if n is less than 2, then n is not a prime number
  if n < 2:
    return False
  
  # Loop through n, check if n is divisible by itself and equal 0, then n is not a prime number
  # for i in range(2, n):
  
  # Optimization
  for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
      return False

  return True

# print(is_prime(1)) # False
# print(is_prime(2)) # True
# print(is_prime(8)) # False
# print(is_prime(11)) # True
# print(is_prime(25)) # False
# print(is_prime(28)) # False