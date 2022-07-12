# Exception ZeroDivisionError: division by zero

# numerator = 10
# denumerator = 0
# print(numerator / denumerator)

# try:
# code that may cause exception
# except:
# code to run when exception occurs

try:
    numerator = int(input('Enter the numerator: '))
    denumerator = int(input('Enter the denumerator: '))

    result = numerator / denumerator
    print(result)

    my_list = [1, 2, 3]
    i = int(input('Enter index: '))
    print(my_list[i])

except ZeroDivisionError:
    print('Denumerator cannot be 0. Please try again')

except IndexError:
    print('Index cannot be greater than the size of the list')

print('Program ends')

# Try - Except - Finally

try:
    print((1 / 0))
except:
    print('Wrong denominator')
finally:
    print('Always printed')

# Using raise keyword

raise KeyboardInterrupt
KeyboardInterrupt

raise MemoryError("This is an argument")
MemoryError

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)


# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)