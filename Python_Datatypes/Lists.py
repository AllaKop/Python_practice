# List is an ordered sequence of items. Mutable.

Languages = ['Python', 'Java', 'Scala', '.NET']

print(Languages[2:])

print(Languages[:2])

print(Languages[-2:])

print(Languages[:-2])

Languages[3] = 'Ruby'
print(Languages)

Languages[0:2] = ['Dart', 'Swift']
print(Languages)

print('Python' in Languages)

for language in Languages:
    print(language)

Languages.append('Rust')
print(Languages)

Languages.insert(1, 'Python')
print(Languages)

Languages.remove('Rust')
print(Languages)

Languages_copy = Languages.copy()
print(Languages_copy)

Nested_list = ['Happy', [100, 200, 300], ['A', 'B', 'C']]
print(Nested_list[0][0])
print(Nested_list[1][0])
print(Nested_list[2][0])

Languages.pop(1)
print(Languages)

Languages_copy.clear()
print(Languages_copy)

a = Languages.index('Scala')
print(a)

# list comprehension

pow2 = [2 ** x for x in range(10)]
print(pow2)

pow3 = [2 ** x for x in range(10) if x > 5]
print(pow3)

pow4 = [x for x in range(20) if x % 2 == 1]
print(pow4)

team1 = ['Janet', 'Arya', 'Mary']
team2 = ['Evan', 'Jake', 'Randy']

new_list = [(x, y) for x in team1 for y in team2]
print(new_list)

number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

num_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(num_list)

obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

#lambda function for lists

letters = list(map(lambda x: x, 'human'))
print(letters)



