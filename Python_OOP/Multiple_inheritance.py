# A class can be derived from more than one base class in Python.
# In multiple inheritance, the features of all the base classes are inherited into the derived class.
# We can also inherit from a derived class. This is called multilevel inheritance.
# In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.

class Animals:

    def eat(self):
        print('I can eat')


class Pets(Animals):

    def socialize(self):
        print('I love to be around the human')


class Cats(Pets):

    def purr(self):
        print('Purr-purr-purr')


class Dogs(Pets):

    def bark(self):
        print('Bark-bark-bark')


class Kotopes(Dogs, Cats):
    pass


Lulu = Cats()
Lulu.purr()
Lulu.socialize()
Lulu.eat()

Businka = Kotopes()
Businka.purr()
Businka.bark()

# Every class in Python is derived from the object class. It is the most base type in Python.
# So technically, all other classes, either built-in or user-defined,
# are derived classes and all objects are instances of the object class.

print(issubclass(list, object))

# Output: True
print(isinstance(5.5, object))

# Output: True
print(isinstance("Hello", object))

# search order is [MultiDerived, Base1, Base2, object]
# This order is also called linearization of MultiDerived class,
# and the set of rules used to find this order is called Method Resolution Order (MRO).

print(Kotopes.__mro__)
print(Kotopes.mro())


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
