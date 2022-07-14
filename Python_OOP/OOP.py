# Creating class Student

class Student:

    # Self is used as the first argument

    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    # Creating object and arguments

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student('Harry', 85)
student2 = Student('Janet', 35)
did_pass = student1.check_pass_fail()  # print(student1.check_pass_fail())
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)


# Create a class Complex

class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, number):
        real = self.real + number.real
        imaginary = self.imaginary + number.imaginary
        result = Complex(real, imaginary)
        return result


n1 = Complex(5, 6)
n2 = Complex(-4, 2)
result = n1.add(n2)
print('real = ', result.real)
print('imaginary = ', result.imaginary)


# Creating a class Triangle

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter


triangle1 = Triangle(3, 4, 5)
perimeter = triangle1.get_perimeter()
print(perimeter)


class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
