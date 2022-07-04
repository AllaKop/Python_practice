# String is sequence of characters. Immutable

text = 'Hello there' # string
print(text)

text1 = """Hello there
How are you doing"""
print(text1)

text2 = 'He said, \"What\'s there?\"'
print(text2)

# Slicing. The first index is inclusive. The last is exclusive.

language = 'Python'
print(language[1:4])

# String concatenation

language1 = 'Python'
language2 = 'programing'
print(language1 + ' ' + language2)

# String repeating

print(language * 3)

# for loop

for character in language:
    print(character)

print('P' in language)

text3 = 'I like Python 3'

result = text3.lower()
print(result)

result1 = text3.upper()
print(result1)

result2 = text3.find('Python')
print(result2)

result3 = text3.replace('Python 3', 'Java')
print(result3)

del text

# Iterating through a string
count = 0
for letter in 'Hello World':
    if letter == 'l':
        count += 1
print(count,'letters found')

str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

# Some of the commonly used methods are .format(), lower(), upper(), join(), split(), find(), replace() etc.

