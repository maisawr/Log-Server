import sys
from datetime import datetime
from socket import AF_INET, SOCK_STREAM, socket

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
user_input = sys.argv

# Parse command line arguments starting from second argument
# The first argument is the program's name
# Second argument: file path to save log messages
# Third argument: host IP address
# Fourth argument: port number to connect to server
# for command in range(1, len(user_input)):
file_name = user_input[1]
host_address = user_input[2]
port_number = int(user_input[3])
    
# If no argument is passed, use default file
    # Call function to open and write to the file
# Else, check if argument is valid .txt file
    # If it's a valid file name, call function to open and write to the file
    # Else, show usage message and quit program


# Newtwork connection using TCP
# AF_INET -> IPv4 family
# SOCK_STREAM -> TCP
# with keyword doesn't require the use of close()
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((host_address, port_number))
    s.listen()
    conn, addr = s.accept()


# Open file with a+ access
# If the file doesn't exist, it will create a new file and append to it
# Otherwise, it will append to the existing file
fhand = open(file_name, 'a+')

# Get timestamp for current date and time
current_time = datetime.now()
time_stamp = current_time.timestamp()
date_time = datetime.fromtimestamp(time_stamp)

# Format timestamp
date_time_str = date_time.strftime("%d-%m-%Y %H:%M:%S")

# Get hostname
host_name = socket.gethostname()

# Log message
log_message = "Log message timestamp: " + date_time_str + " hostname: " + host_name + "\n"

# Write log message to file
fhand.write(log_message)

# Close file
fhand.close()

# TO DO
# Refactor code using with open()
# Refactor code to transform open/write file into a function
# Refactor code to use getopt to check command line arguments
# Research about three way handshake
# Research about: If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
# Research: he socket that you’ll use to communicate with the client. It’s distinct from the listening socket that the server is using to accept new connections