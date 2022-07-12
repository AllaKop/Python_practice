import os

# Getting the directory pass

current_dir = os.getcwd()
print(current_dir)

# Change current directory
# os.chdir ('new path')

# Return files inside the directory

print(os.listdir())

# Create new directory

os.mkdir('test')

# Rename files

os.rename('test', 'test_new')

# Removing directory or file

os.rmdir('test_new')



