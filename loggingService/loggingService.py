from concurrent.futures import thread
from email import message_from_string
import sys
from datetime import datetime
from socket import *
import os
from _thread import *
from writeLog import *

# REQUIREMENTS
# file's name can't be hardcoded
# include in a config file
# argument line command?
# logs must be saved in a plain text file
# how to format the message? Client choose a format as command line argument. Options: syslog (default) or JSON
# how to identify levels? Client send the level in the request
# how to connect to other device (TCP/UDP)? TCP connection.
# how transform into a service? No need to transform into a windows service.
# how to connect to several clients? selectors or asyncio?




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
log_format = user_input[4]
message = ""
thread_count = 0

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

    with conn:
        print(f"Conected to {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            # Get request
            message = data.decode()
            conn.sendall(data)

        writeLog(file_name, message, addr)
       
        
    



if (log_format == "json"):
    pass
else:
    pass


# TO DO
# Check for errors using try catch
# Refactor code using with open()
# Refactor code to transform open/write file into a function
# Refactor code to use getopt to check command line arguments
# Research about three way handshake
# Research about: If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
# Research: he socket that you’ll use to communicate with the client. It’s distinct from the listening socket that the server is using to accept new connections