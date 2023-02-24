import sys
from socket import *
import os
import types
from writeLog import *
from parseArguments import parseArguments
import selectors

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

# Call parseArguments() function to get the command line arguments
args = parseArguments()

# Create a selector to support multi connections
selector = selectors.DefaultSelector()

# Global variable to hold the client request in a string type
message = ""

# Accept client socket
def accept_client(sock):
    
    conn, addr = sock.accept()

    print(f"Conected to {addr}")

    conn.setblocking(False)                                             # enable non-blocking mode
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE               # check if the client is ready to read or write
    selector.register(conn, events, data=data)

# Request from and response to client 
def service_connection(key, mask):
    client_socket = key.fileobj                 # define client according to tuple created it in accept_client()
    data = key.data                             # get data for specific client

    # Receive request from client
    if mask & selectors.EVENT_READ:
        recv_data = client_socket.recv(1024)                

        if recv_data:                                       # check if there's any data to receive                           
            data.outb += recv_data                          # store data received in data             
        else:                                               # when there's no data left to receive, close the connection
            print(f"Closing connection to {data.addr}")
            selector.unregister(client_socket)
            client_socket.close()
    


    # Send response to client
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = client_socket.send(data.outb)
            data.outb = data.outb[sent:]                    # discard the bytes sent from the buffer










# Newtwork connection using TCP
# AF_INET -> IPv4 family
# SOCK_STREAM -> TCP
# with keyword doesn't require the use of close()
with socket(AF_INET, SOCK_STREAM) as s:
    
    s.bind((args.IP_address, args.port_number))
    s.listen()
    s.setblocking(False)                                    # prevent blocking the server when the socket is called
    selector.register(s, selectors.EVENT_READ, data=None)   # monitor the listening socket using the .EVENT_READ and track the data

    # Event loop to monitor the sockets ready for I/O
    try:
        while True:
            events = selector.select(timeout=None)          # block until there's a socket ready
            for key, mask in events:                        # tuple with a socket and the operations that are ready
                if key.data is None:                        # if data is None, accept a new socket
                    accept_client(key.fileobj)
                else:
                    pass
                    service_connection(key, mask)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        selector.close()


    #conn, addr = s.accept()

    #with conn:
    #    print(f"Conected to {addr}")
    #    while True:
    #        data = conn.recv(1024)
    #        if not data:
    #            break

    #        # Get request
    #        message = data.decode()
    #        conn.sendall(data)
        
    #    # Call function to write log message formatted
    #    logger(args.file, message, args.json)
 
        



# TO DO
# Check for errors using try catch
# Refactor code using with open()
# Refactor code to transform open/write file into a function
# Refactor code to use getopt to check command line arguments
# Research about three way handshake
# Research about: If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
# Research: he socket that you’ll use to communicate with the client. It’s distinct from the listening socket that the server is using to accept new connections
# Do we need this for the logging service: events = selectors.EVENT_READ | selectors.EVENT_WRITE?