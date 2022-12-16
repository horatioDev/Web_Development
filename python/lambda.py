# Define a list of people
people= [ 
  { 'name': 'Ray', 'house': 'Vampire'},
  { 'name': 'Xavier', 'house': 'Werewolf'},
  { 'name': 'Mystery', 'house': 'Hybrid'},
]


# Sort people
# people.sort() # TypeError: '<' not supported between instances of 'dict' and 'dict'

# Define a function that tells the sort function what parameters to use when sorting
def f(person):
  return person['name']


# people.sort(key=f) # [{'name': 'Mystery', 'house': 'Hybrid'}, {'name': 'Ray', 'house': 'Vampire'}, {'name': 'Xavier', 'house': 'Werewolf'}]

# Lambda function
people.sort(key=lambda person: person['name'])


# Print
print(people)