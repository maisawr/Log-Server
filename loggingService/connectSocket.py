import types
import selectors
from socket import *
from writeLog import logger
from parseArguments import parse_arguments

# Call parseArguments() function to get the command line arguments
args = parse_arguments()

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
def service_connection(key, mask, args, message):
    client_socket = key.fileobj                 # define client according to tuple created it in accept_client()
    data = key.data                             # get data for specific client

    # Receive request from client
    if mask & selectors.EVENT_READ:
        recv_data = client_socket.recv(1024)                

        if recv_data:                                       # check if there's any data to receive                           
            data.outb += recv_data                          # store data received in data   
            
            # Decode the request to string 
            message = data.outb.decode()
        
            # Call function to write log message formatted
            logger(args.file_name, message, args.json)

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
def start_server():
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
                        service_connection(key, mask, args, message)
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")
        finally:
            selector.close()
