# Server
import os
import socket

import Config
from cryptography.fernet import Fernet

s = socket.socket()
print('Socket created')
s.bind((Config.server_address, Config.port_number))
s.listen(3)
print('Waiting for connections')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with ", addr, name)
    data = c.recv(1024).decode()
    c.send(bytes('Welcome to the dictionary', 'utf-8'))


# Decoding file from client
def decode_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
