# Server
import socket
from dict2xml import dict2xml
import Config
import sys
import json
import pickle
from cryptography.fernet import Fernet

COUNTRIES = Config.countries

s = socket.socket()
print('Socket created')
s.bind((Config.server_address, Config.port_number))
s.listen(3)  # take it out or put it into the config file (config.timeout(3))
print('Waiting for connections')


# Deserialization
def des(deserialization):
    if Config.deserialization_option == "JSON":
        return json.loads(deserialization)

    elif Config.deserialization_option == "BINARY":
        return pickle.loads(deserialization)

    elif Config.deserialization_option == "XML":
        return dict2xml(deserialization, wrap="dictionary", indent="  ")

    else:
        print("format not recognised")


def decrypt():
    f = Fernet(Config.key)
    text = input("GrpC.txt").encode()
    encrypted = f.encrypt(text)
    decrypted = f.decrypt(encrypted)


while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()  # put the number into the config file # print("connected with ", addr, name)
    if Config.opt == 1:
        print(name)
    else:
        sys.exit()

    c.send(bytes('Welcome to the dictionary', 'utf-8'))  # messages into the config file
    c.close()
