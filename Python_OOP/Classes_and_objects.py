class Person:

    def __init__(self, name, age, sex, high, weight):
        self.name = name

        self.age = age
        self.sex = sex
        self.high = high
        self.weight = weight

    def greet(self):
        print('Hello')

    def introduce(self) -> object:
        print('I am', self.name, self.age, self.sex, self.high, self.weight)


Alla = Person('Alla', 27, 'female', 162, 54)
Alla.greet()  # Alla.greet() = Person.greet(Alla)
Alla.introduce()


# Class functions that begin with double underscore __ are called special functions as they have special meaning.
# Of one particular interest is the __init__() function.
# This special function gets called whenever a new object of that class is instantiated.

class ComplexNumber:

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10
num2.get_data()

# Output: (5, 0, 10)
print((num2.real, num2.imag, num2.attr))

# Delete statement for attribute
del num2.attr
print((num2.real, num2.imag, num2.attr))

# Delete statement for object
del num2
num2.get_data()
