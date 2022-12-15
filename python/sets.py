# Set: collection of unique values (No repeats)

# Create an empty set
s = set()

# Add to set
s.add(1)
s.add(3)
s.add(2)
s.add(4)
s.add(5)
s.add(6)

print(s) # {1, 2, 3, 4, 5, 6}

s.add(4)
s.add(3)

print(s) # {1, 2, 3, 4, 5, 6}

# Remove from set
s.remove(4)

print(s) # {1, 2, 3, 5, 6}

# Get the length of set
print(f'The set has {len(s)} elements.') 