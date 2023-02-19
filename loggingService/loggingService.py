import sys

# REQUIREMENTS
# file's name can't be hardcoded
# include in a config file
# argument line command?
# logs must be saved in a plain text file
# how to format the message?
# how to identify levels?
# how to connect to other device (TCP/UDP)?
# how transform into a service?


# Get arguments from command line
userInput = sys.argv

# Parse command line arguments starting from second argument
# The first argument is the program's name
for command in range(1, len(userInput)):
    fileName = sys.argv[1]
    
# If no argument is passed, use default file
    # Call function to open and write to the file
# Else, check if argument is valid .txt file
    # If it's a valid file name, call function to open and write to the file
    # Else, show usage message and quit program

# Open file with a+ access
# If the file doesn't exist, it will create a new file and append to it
# Else, it will append to the existing file
fhand = open(fileName, 'a+')
fhand.write("Write log message")
fhand.close()

# TO DO
# Refactor code using with open()
# Refactor code to transform open/write file into a function

