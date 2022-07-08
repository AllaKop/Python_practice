# Dictionary is unordered sequence of items with a key.
# Keys have to be of immutable type and unique.

#dictionaries comprehension

numbers = [1, 2, 3, 4, 5,]

square_dict = dict()

for num in numbers:
    square_dict[num] = num**2

print(square_dict)

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

new_price = {key: value * 1.5 if value > 2 else value for (key, value) in old_price.items()}
print(new_price)

# Creating of a dictionary
person = {'Name': 'Linux', 'Age': 21}
print(person)
print(person['Name'])
print(person.get('Hobbies'))

# Change value

person['Name'] = 'Denise'
print(person)

# Adding items

person['Hobby'] = 'Dancing'
print(person)

# For loop

for key in person:
    print(key)

# We can remove a particular item in a dictionary by using the pop() method.
# This method removes an item with the provided key and returns the value.

print(person.pop('Hobby'))
print(person)

# Dictionary Comprehension

squares = {x: x*x for x in range(6)}
print(squares)

# Dictionary Comprehension with if conditional

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)

# Iterating through a Dictionary

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])



