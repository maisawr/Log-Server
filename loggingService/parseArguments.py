#TO DO
# If no argument is passed, use default file
    # Call function to open and write to the file
# Else, check if argument is valid .txt file
    # If it's a valid file name, call function to open and write to the file
    # Else, show usage message and quit program


import argparse
import os



# Parse command line arguments using argparse
# Include usage message
# Required arguments are the IP address and the port number
# The file name and the format are optional
# Return a list with the arguments' values

def parse_arguments():
    parser = argparse.ArgumentParser(description="Log messages from client in a chosen format.")

    # Define arguments
    parser.add_argument("IP_address", help="IP address to start connection")
    parser.add_argument("port_number", help="port number where the server is listening", type=int)
    parser.add_argument("-f", "--file", help="determine a file to save the log. The default is log.txt")
    parser.add_argument("-j", "--json", help="define the message format as json. The default is syslog format", 
                        action="store_const", const="JSON")
    
    # Store arguments' values in args
    args = parser.parse_args()

    # Check if the user entered a text file name
    # Validate if the file has a .txt extension
    # If the user didn't define a file's name, the defualt is log.txt
    if (args.file):
        base, ext = os.path.splitext(args.file)
        if (ext.lower() != '.txt'):
            parser.print_help()
            raise argparse.ArgumentTypeError('File must have a txt extension')
    else:
        args.file = "log.txt"

    return args
