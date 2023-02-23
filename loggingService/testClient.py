import socket
import platform
import os

HOST = "192.168.2.228"
PORT = 3000

host_name = platform.node()
process_id = os.getppid()
print(process_id)

log_level = "INFO"
log_message = f"{host_name}: {log_level}: {process_id}: Testing again format" 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(log_message.encode())
    data = s.recv(1024)

print(f"Received {data!r}")