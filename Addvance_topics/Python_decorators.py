# A decorator takes in a function, adds some functionality and returns it.

def inc(x):
    return x + 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))


def display_info(func):
    def inner():
        print("Executing", func.__name__, 'function')
        func()
        print('Finished execution')

    return inner()


""" def printer():
    print('Hello world!')
display_info(printer)"""


@display_info
def printer():
    print('Hello, World!')


# Creating a decorator for functions with some parameters

def smart_divide(func):
    def inner(a, b):
        print('Dividing', a, 'by', b)
        if b == 0:
            print('Cannot divide by 0')
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a / b


value1 = divide(15, 3)
print(value1)

value2 = divide(5, 0)
print(value2)

# Multiple decorators can be chained in Python.
# This is to say, a function can be decorated multiple times with different (or same) decorators.


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

