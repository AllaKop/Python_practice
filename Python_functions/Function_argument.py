# Creating the greet function

def greet(name):
    print('Hello', name)
    print('How do you do? ')


greet(input('Enter your name '))


# Creating the multiplication function for two arguments

def add_two_numbers(number_1: int, number_2: int):
    result = number_1 + number_2
    print('The sum is ', result)


add_two_numbers(int(input('Enter the first number ')), int(input('Enter the second number ')))

'''Grading Student Based on Marks Obtained by Making Functions
Suppose you just attended a University examination.
The marks you obtained in various subjects are stored in a list like this:

marks = [55, 64, 75, 80, 65]
You want to find the average marks you obtained in the exam.

Based on the average marks you want to find your grade as:
You will get Grade A if the average marks is equal to or above 80
You will get Grade B if the average marks is equal to or above 60 and less than 80
You will get Grade C if the average marks is equal to or above 50 and less than 60
And if the average marks is less than 50, you will get Grade F'''

marks = [float(input('Enter your first mark ')), float(input('Enter your second mark ')),
         float(input('Enter your third mark '))]


# creating a function to calculate the average
def calculate_average_mark(marks):
    total_of_marks = sum(marks)
    quantity_of_marks = len(marks)
    result = total_of_marks / quantity_of_marks
    return result


def compute_grade(average_mark):
    if average_mark >= 80:
        grade = 'A'
    elif 60 <= average_mark < 80:
        grade = 'B'
    elif 50 <= average_mark < 60:
        grade = 'C'
    else:
        grade = 'F'
    return grade


average_mark = calculate_average_mark(marks)
grade = compute_grade(average_mark)

print('You average mark is ', average_mark)
print('You grade is ', grade)

'''Can you create a program to add and multiply two numbers?
For this, create two functions add_numbers() and multiply_numbers().
These functions should compute the result and return them to the function.
Call and should print from outside the function.'''


def add_numbers(n1, n2):
    return n1 + n2


def multiply_numbers(n1, n2):
    return n1 * n2


number1 = int(input('Enter the first number '))
number2 = int(input('Enter the second number '))

adding = add_numbers(number1, number2)
multiplying = multiply_numbers(number1, number2)

print('The sum is ', adding)
print('The multiplication is ', multiplying)
