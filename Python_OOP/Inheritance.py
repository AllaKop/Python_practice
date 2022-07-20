# Inheritance is a way of creating a new class for using details of an existing class without modifying it.

# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        # Additionally, we use the super() function inside the __init__() method.
        # This allows us to run the __init__() method of the parent class inside the child class.
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


class Animal:

    def eat(self):
        print('I can eat')


class Dog(Animal):

    def bark(self):
        print('I can bark')


class Cat(Animal):

    def get_grumpy(self):
        print('I am grumpy')


Baron = Dog()
Baron.bark()
Baron.eat()
Lulu = Cat()
# Lulu.bark
Lulu.eat()
Lulu.get_grumpy()


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.input_sides()
t.disp_sides()
t.find_area()
print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, int))
print(isinstance(t, object))
print(issubclass(Polygon, Triangle))
print(issubclass(Triangle, Polygon))
print(issubclass(bool, int))
