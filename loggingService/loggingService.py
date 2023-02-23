from concurrent.futures import thread
import sys
from socket import *
import os
from _thread import *
from writeLog import *
import argparse
from parseArguments import parseArguments

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

args = parseArguments()

message = ""
thread_count = 0

# Newtwork connection using TCP
# AF_INET -> IPv4 family
# SOCK_STREAM -> TCP
# with keyword doesn't require the use of close()
with socket(AF_INET, SOCK_STREAM) as s:
    
    s.bind((args.IP_address, args.port_number))
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
        
        # Call function to write log message formatted
        logger(args.file, message, args.json)
       

# TO DO
# Check for errors using try catch
# Refactor code using with open()
# Refactor code to transform open/write file into a function
# Refactor code to use getopt to check command line arguments
# Research about three way handshake
# Research about: If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
# Research: he socket that you’ll use to communicate with the client. It’s distinct from the listening socket that the server is using to accept new connections