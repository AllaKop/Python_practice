# Tuple is ordered sequence of items. Immutable

Tuple = (1, 2, 4, 'Hello')
print(Tuple)

# same rules as for lists.
# immutable, cannot be changed

mixed_list = ['Hello', -34, 'Java', True]
print('1.', mixed_list[-1])

mixed_list[1] = 'Hi'
print('2.', mixed_list)

mixed_tuple = (1, 3, 4, 5)
print('3.', mixed_tuple)

print('4. ', len(mixed_tuple))

# A tuple can also be created without using parentheses. This is known as tuple packing.
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog

my_tuple = ("hello")
print(type(my_tuple))  # class 'str'

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # class 'tuple'

# Parentheses are optional
my_tuple = "hello",
print(type(my_tuple))  # class 'tuple'

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4
print(n_tuple[2][1])      # 2

# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])

# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

# Can delete an entire tuple
del my_tuple

# Tuple's methods

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3
print('a' in my_tuple)

