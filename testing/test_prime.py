# This file is used for testing the is_prime function

# Import is_prime function
from prime import is_prime

def test_prime_function(n, expected):
  # Check if is_prime is not equal to expected
  if is_prime(n) != expected:
    print(f"ERROR on is_prime({n}), expected {expected}")