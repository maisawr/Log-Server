# Filename: loggingService.py
# Project: loggingService
# By: Maísa Wolff Resplande, student ID 8778967
# Date: Feb 24, 2023
# Description: This program runs a log server. The client should connect to it using TCP/IP. 
#              It supports multi-client connections and more the one log format per session. 
#              The logs of all clients are written in a .txt file. 
#              Because of the network connection, it can be used as a remote log server.
#              The log server is configured through command line arguments containing the IP address, the port number, 
#              the file name to log the messages, and optionally a different log format than the default. 
#              The default log format is Syslog format, and the other optional is JSON.

# REQUIREMENTS
# file's name can't be hardcoded
# include in a config file or argument line command? Argument line command
# logs must be saved in one plain text file for all client. It's possible to have different files for different log formats
# how to format the message? Client choose a format as command line argument. Options: syslog (default) or JSON
# how to identify levels? Client send the level in the request?
# how to connect to other device (TCP/UDP)? TCP connection.
# how transform into a service? No need to transform into a windows service.
# how to connect to several clients? selectors or asyncio? Selectors

# TO DO
# Check for errors using try catch
# Refactor code using with open() OK
# Refactor code to transform open/write file into a function OK
# Refactor code to use getopt to check command line arguments USING argparse
# Research about three way handshake
# Research about: If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
# Research: he socket that you’ll use to communicate with the client. It’s distinct from the listening socket that the server is using to accept new connections
# Do we need this for the logging service: events = selectors.EVENT_READ | selectors.EVENT_WRITE?

#- rate limiter
#- error handling
#- filter log levels
#- identify clients
#- write READ ME for server


from connectSocket import start_server

# Start program
start_server()
