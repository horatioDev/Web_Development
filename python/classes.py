# Object-Oriented Programming

# Define a class/template for Point
class Point():
  # Method that references this object
  def __init__(self, input1, input2):
    self.x = input1
    self.y = input2

# Create a new point object
p = Point(2, 8) #Point(input1, input2)

# Print
print(p.x)
print(p.y)

# Define a class/template for Flight
class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  # Def func that adds a passenger to flight list by name
  def add_passenger(self, name):
    # Check if any open seats
      # If not return False
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True

  # Define a func that returns the amount of seat available
  def open_seats(self):
    return self.capacity - len(self.passengers)

# Create Flight object 
flight = Flight(3)

# List of people
people = ['Ray', 'Xavier', 'Tranq', 'Mystery']

# Loop through and add person to flight if enough space
for person in people:
  # Variable to hold seats available
  seats = flight.open_seats()
  # Check if passenger was added successfully
  if flight.add_passenger(person):
    print(f'{seats} seats available')
    print(f'Added {person} to flight successfully')
  else:
    print(f'No available seats for {person}')