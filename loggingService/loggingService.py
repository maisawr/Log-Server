import sys

# TO DO
# file's name can't be hardcoded
# include in a config file
# prompt user to write the file's name?
# argument line command?

fileName = input("Enter the file's name: ")

# Open file with a+ access
# If the file doesn't exist, it will create a new file and append to it
# Else, it will append to the existing file
fhand = open(fileName, 'a+')
fhand.write("Write log message")
fhand.close()

# TO DO
# Refactor code using with open()
