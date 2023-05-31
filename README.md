# Log-Server
Authors: Maísa Wolff Resplande and Hyewon Lee
Date: Feb 24th, 2023

# Log Server Description
This project implements a log server and a test client. The client should connect to the server using TCP/IP. 
The server supports multi-client connections and one log format per session. The default log format is Syslog format, and the other optional is JSON. 
The logs of all clients are written in a .txt file. Because of the network connection, it can be used as a remote log server. 
The log server is configured through command line arguments containing the IP address, the port number, the file name to log the messages, 
and optionally a different log format than the default.

How to run the server: 
1 - On the shell, type python3 loggingService.py with the required arguments 
2 - The required arguments are: IP address, port number and file name with .txt extension
3 - The -h or --help provide usage 
4 - The -j or --json change the log format to JSON string

# Test Client Description
The test client performs a set of automated tests sending log messages to the server. 
It's configured through command line arguments containing the IP address and the port number.

How to run the client: 
1 - On the shell, type Client.exe with the required arguments 
2 - The required arguments are: IP address and port number
