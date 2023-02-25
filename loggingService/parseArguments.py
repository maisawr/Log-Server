# Filename: parseArguments.py
# Project: loggingService
# By: Maísa Wolff Resplande, student ID 8778967
# Date: Feb 24, 2023
# Description: This file define the function to parse the command line arguments.



import argparse
import os
import sys



# Parse command line arguments using argparse
# Include usage message
# Required arguments are the IP address, the port number and the file name
# The log format is optional
# Return a list with the arguments' values
def parse_arguments():
    parser = argparse.ArgumentParser(description="Log messages from client in a chosen format.")

    # Define arguments
    parser.add_argument("IP_address", help="IP address to start connection")
    parser.add_argument("port_number", help="port number where the server is listening", type=int)
    parser.add_argument("file_name", help="determine a .txt file to save the log")
    parser.add_argument("-j", "--json", help="define the message format as json. The default is syslog format", 
                        action="store_const", const="JSON")
    
    # Store arguments' values in args
    args = parser.parse_args()

    # Check if the user entered a text file name
    # Validate if the file has a .txt extension
    # If the user didn't define a file's name, the defualt is log.txt
    if (args.file_name):
        base, ext = os.path.splitext(args.file_name)
        if (ext.lower() != ".txt"):
            parser.print_help()
            sys.exit("\nERROR: File must have a .txt extension")

    return args
