# Set is unordered sequence of unique items.
# Set is mutable, but can contain only immutable items like Strings, Tuples, Numbers.

#set comprehension

word = 'programing'

alphabets = {x for x in word}
print(alphabets)

# Creating a set

animal = {'Tiger', 'Panther', 'Lion'}
print(animal)

# Add element to the set
animal.add('Monkey')
print(animal)

# Update one set with another one

pets = {'Cat', 'Dog'}
animal.update(pets)
print(animal)

# Removing item from the set
# The only difference between the two is that the discard() function leaves a set unchanged
# if the element is not present in the set.
# On the other hand, the remove() function will raise an error
# in such a condition (if element is not present in the set).

animal.remove('Dog')
animal.discard('Monkey')
print(animal)

# Removing all items

animal.clear()
print(animal)

# Union function

domestic_animals = {'Dog', 'Cat', 'Parrot'}
wild_animals = {'Lion', 'Tiger', 'Parrot'}
animals = domestic_animals.union(wild_animals)
print(animals)

# Intersection

domestic_animals1 = {'Dog', 'Cat', 'Parrot'}
wild_animals1 = {'Lion', 'Tiger', 'Parrot'}
animals1 = domestic_animals1.intersection(wild_animals1)
print(animals1)

# Difference

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.difference(B))

# Set Symmetric Difference

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.symmetric_difference(B))

# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.
# Sets being mutable are unhashable, so they can't be used as dictionary keys.
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.

A1 = frozenset([1, 2, 3, 4])
B2 = frozenset([3, 4, 5, 6])
print(type(A1))









