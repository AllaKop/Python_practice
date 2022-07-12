f = open('message.txt')

# open and read the file
# r - read mode
# w - write mode
# a - append mode

content = f.read()
print(content)

f.close()

# First 6 characters will be read

f = open('message.txt')

content = f.read(6)
print(content)

f.close()

# Using with operator so not to use close

with open('message.txt') as f:
    content = f.read(6)
    print(content)

    more_content = f.read(8)
    print(more_content)

# Using write mode

with open('message.txt', 'w') as f:
    content = f.write('Telling the truth I love cats')
    print(content)

# Using append mode

with open('message1.txt', 'a') as f:
    content = f.write('\nI like Python\nI like coding')
    print(content)



