# Reading the entire file
with open('C:\\Users\\Admin\\OneDrive\\Desktop\\newrepo\\poem.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('C:\\Users\\Admin\\OneDrive\\Documents\\Python Scripts\\poem.txt', 'r') as file:
    for line in file:
        print(line, end='')



# Writing to a file
with open('C:\\Users\\Admin\\OneDrive\\Documents\\Python Scripts\\poem.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("Writing to a file in Python.")

# Appending to a file
with open('C:\\Users\\Admin\\OneDrive\\Documents\\Python Scripts\\poem.txt', 'a') as file:
    file.write("\nAppending a new line.")


#2. Reading and Writing Binary Files
#Reading Binary Files
#Binary files can be read using the mode 'rb'.
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)
#Writing Binary Files
#Binary files can be written using the mode 'wb'
data = b"Binary data"

with open('example.bin', 'wb') as file:
    file.write(data)




#3. Importing os Module for Directory Management
#The os module provides a way to interact with the operating system. This includes directory management.

import os

# Get current working directory
cwd = os.getcwd()
print("Current Directory:", cwd)

# Create a new directory
os.mkdir('new_directory')

# Change directory
os.chdir('new_directory')
print("Changed Directory:", os.getcwd())

# List files and directories
print("Directory Contents:", os.listdir('.'))

# Remove directory
os.chdir('..')
os.rmdir('new_directory')
print("Directory 'new_directory' removed.")




#. Saving Structured Data with JSON
#JSON (JavaScript Object Notation) is a 
#lightweight data interchange format. Python provides the json module to work with JSON data.
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file)




with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)



import os
import json

# Directory management
os.mkdir('example_dir')
os.chdir('example_dir')

# Writing text file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a text file.\nSecond line.")

# Reading text file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Text File Content:\n", content)

# Writing binary file
with open('example.bin', 'wb') as file:
    file.write(b'This is binary data.')

# Reading binary file
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print("Binary File Content:", binary_content)

# Writing JSON data
data = {"key1": "value1", "key2": "value2"}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON data
with open('data.json', 'r') as file:
    json_data = json.load(file)
    print("JSON File Content:", json_data)

# Cleanup
os.chdir('..')
os.rmdir('example_dir')





