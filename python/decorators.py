# Decorators(Function Programming): a function that takes in a function as an input

'''
Define a function that takes a function as input
  That modifies a function
  Returns when function is about to run
  Runs input function
  Returns when function is completed running
'''

# Decorator function
def announce(f):
  def wrapper():
    print('About to run function.')
    f()
    print('Done with function.')
  return wrapper

# Decorator
@announce
def hello():
  print('Hello, world!')

# Call hello function
hello()