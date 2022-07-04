# Dictionary is unordered sequence of items with a key.

#dictionaries comprehension

numbers = [1, 2, 3, 4, 5,]

square_dict = dict()

for num in numbers:
    square_dict[num] = num**2

print(square_dict)

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

new_price = {key: value * 1.5 if value > 2 else value for (key, value) in old_price.items()}
print(new_price)