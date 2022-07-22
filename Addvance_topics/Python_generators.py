def generate_fibonacci():
    n1 = 0
    n2 = 1

    while True:
        yield n1
        n1, n2 = n2, n1 + n2


seq = generate_fibonacci()
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

"""Anonymous generator functions"""

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

# Initialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))

next(a)




