Tuple = (1, 2, 4, 'Hello')

print(Tuple)

# same rules as for lists.
# immutable, cannot be changed

mixed_list = ['Hello', -34, 'Java', True]
print('1.', mixed_list[-1])

mixed_list[1] = 'Hi'
print('2.', mixed_list)

mixed_tuple = (1, 3, 4, 5)
mixed_tuple[1] = 100
print('3.', mixed_tuple)