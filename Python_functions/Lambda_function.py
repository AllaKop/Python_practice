# Calculating n square

square = lambda n: n * n

print(square(10))

# Factorial of an integer

factorial = lambda x: 1 if x == 1 else x * factorial(x - 1)

print(factorial(5))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)