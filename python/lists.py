# List: sequence of mutable/changeable values

# Define a list of names
names = ['Ray', 'Xavier', 'Mystery', 'Tranq']

print(names) # ['Ray', 'Xavier', 'Mystery', 'Tranq']
print(names[0]) # ['Ray']
print(names[3]) # ['Tranq']
# print(names[6]) # IndexError: list index out of range

# Add a name to end of list
names.append('Python')

print(names) # ['Ray', 'Xavier', 'Mystery', 'Tranq', 'Python']

# Sort names alphabetically
names.sort()

print(names) # ['Mystery', 'Python', 'Ray', 'Tranq', 'Xavier']

# Get the length of list
print(f'The list has {len(names)} elements.') 