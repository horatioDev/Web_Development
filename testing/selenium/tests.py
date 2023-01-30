# Import os for Browser ...
import os
# Import pathlib for ...
import pathlib
# Import unittest for testing
import unittest

# Import webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# Define file url path
def file_uri(filename):
  return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()


# Define Webpage Tests
class WebpageTests(unittest.TestCase):

  # Test title
  def test_title(self):
    driver.get(file_uri("counter/counter.html"))
    self.assertEqual(driver.title, "Counter")

  # Test Increase Count
  def test_increase(self):
    driver.get(file_uri("counter/counter.html"))
    increase = driver.find_element(By.ID, "increase")
    increase.click()
    self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "1")
  
  # Test decrease Count
  def test_decrease(self):
    driver.get(file_uri("counter/counter.html"))
    decrease = driver.find_element(By.ID, "decrease")
    decrease.click()
    self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

  # Test multiple increase
  def test_multiple_increase(self):
    driver.get(file_uri("counter/counter.html"))
    increase = driver.find_element(By.ID, "increase")

    # loop through a range of n = 3
    for n in range(3):
      increase.click()
    
    # Assert increase = 3
    self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "3")
  
  # Test multiple decrease
  def test_multiple_decrease(self):
    driver.get(file_uri("counter/counter.html"))
    decrease = driver.find_element(By.ID, "decrease")

    # loop through a range of n = 3
    for n in range(3):
      decrease.click()
    
    # Assert increase = 3
    self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-3")


if __name__ == "main":
  unittest.main()