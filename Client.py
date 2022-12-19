import json
import pickle
import dict2xml as dict2xml
import Config
import socket
from dict2xml import dict2xml
from cryptography.fernet import Fernet

COUNTRIES = Config.countries

s = socket.socket()
client = socket.socket()
client.connect((Config.server_address, Config.port_number))


# Serialization/ pickle file
def serialise_dictionary(serialization):
    if Config.serialization_option == "JSON":
        return json.dumps(serialization)

    elif Config.serialization_option == "BINARY":
        return pickle.dumps(serialization)

    elif Config.serialization_option == "XML":
        return dict2xml(serialization, wrap="dictionary", indent="  ")

    else:
        print("format not recognised")


payload = serialise_dictionary(COUNTRIES)
client.send(payload.encode('utf8'))

with open('GrpC.txt', 'w') as data:
    data.write(str(COUNTRIES))


# File encryption
def encrypt():
    f = Fernet(Config.key)
    text = input("GrpC.txt").encode()
    encrypted = f.encrypt(text)
    print("Encrypted dictionary")
