# Import unittest library for class definition
import unittest

# Import function to be tested
from prime import is_prime

# Define a Test class w/ TestCase as an argument
"""
How to run tests in terminal:
  Examples:
  py.exe -m unittest test_module    - run tests from test_module

  - "py.exe -m unittest module.TestClass   - run tests from module.TestClass"

  py.exe -m unittest module.Class.test_method   - run specified test method
  py.exe -m unittest path/to/test_file.py   - run tests from test_file.py
  
  python.exe -m unittest test_module    - run tests from test_module

  - "python.exe -m unittest module.TestClass   - run tests from module.TestClass"

  python.exe -m unittest module.Class.test_method   - run specified test method
  python.exe -m unittest path/to/test_file.py   - run tests from test_file.py
"""
class Tests(unittest.TestCase):

  # Define function(s) for each thing to be tested
  def test_1(self):
    """Check that 1 is not prime"""
    self.assertFalse(is_prime(1))
  
  def test_2(self):
    """Check that 2 is prime"""
    self.assertTrue(is_prime(2))
  
  def test_8(self):
    """Check that 8 is not prime"""
    self.assertFalse(is_prime(8))
  
  def test_11(self):
    """Check that 11 is prime"""
    self.assertTrue(is_prime(11))
  
  def test_25(self):
    """Check that 25 is not prime"""
    self.assertFalse(is_prime(25))
  
  def test_28(self):
    """Check that 28 is not prime"""
    self.assertFalse(is_prime(28))

# Run function if this program is runned/called
if __name__ == "main":
    unittest.main() 

# Output
"""
  py -m unittest tests.Tests

  ...F.F
  ======================================================================
  FAIL: test_25 (tests.Tests)
  Check that 25 is not prime
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\testing\tests.py", line 37, in test_25
      self.assertFalse(is_prime(25))
  AssertionError: True is not false

  ======================================================================
  FAIL: test_8 (tests.Tests)
  Check that 8 is not prime
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\testing\tests.py", line 29, in test_8
  ----------------------------------------------------------------------
  Ran 6 tests in 0.002s

  FAILED (failures=2)
"""