# The first task

count: int = 0
while count <= 10:
    print(count)
    count += 1

# The second task
number = int(input('Enter any number '))

while number <= 10:
    print('The number is in the loop')
    number += 1
else:
    print('The number is out the loop')

# The multiplication table
number = int(input('Enter the number '))

count = 1
while count <= 10:
    product = number * count
    print(number, 'x ', count, '= ', product)
    count += 1

# The multiplication table from big to small

number = int(input('Enter the number '))

count = 10
while 10 >= count > 0:
    product = number * count
    print(number, 'x', count, '=', product)
    count -= 1

# The sum of all number from 0 till n.

n = int(input('Enter n '))
sum_of_all_numbers = 0
i = 1
while i <= n:
    sum_of_all_numbers = sum_of_all_numbers + i
    i = i + 1
print('Sum is ', sum_of_all_numbers)





