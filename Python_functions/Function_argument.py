# Positional arguments assigned based on the position

def add_numbers(n1, n2):
    sum_of_numbers = n1 + n2
    return sum_of_numbers


result = add_numbers(5.6, 5.4)
print(result)


# Default argument assigned in the function definition

def add_numbers(n1=100, n2=1000):
    sum_of_numbers = n1 + n2
    return sum_of_numbers


result = add_numbers(5.6)
print(result)


# Keyword arguments

def greet(name, message):
    print('Hello, ', name)
    print(message)


greet(name='Alla', message='Howdy?')


# Arbitary parameters

def greet(*names):
    for name in names:
        print('Hello', name)


greet('Alla, ', 'Kolia, ', 'Lulu, ', 'Businka!')
