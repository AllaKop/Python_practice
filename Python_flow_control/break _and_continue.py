for item in range(1, 9):
    if item == 3:
        break
    print(item)
print('The end')

# The second task

while True:
    number = float(input('Enter the number '))
    if number < 0:
        break
    print('You entered number ', number)
    break

# The third task
for i in range(1, 5):
    number = float(input('Enter the number '))
    if number == i:
        print(number)
    else:
        print('Out of the range')
    break

# Create the program so that all items of the languages in the list are printed except Swift and c++.
# languages = ['Python', 'Java', 'Swift', 'C', 'C++']

languages = ['Python', 'Java', 'Swift', 'C', 'C++']
for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)


