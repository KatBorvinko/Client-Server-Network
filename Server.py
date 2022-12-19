# Importing libraries
import json
import pickle
from pickle import dumps, loads, load, dump
from dict2xml import dict2xml
from cryptography.fernet import Fernet
import Config
import socket

# Prepare the server to the connection with the client
s = socket.socket()
print('Socket created')
s.listen(3)
print('Waiting for connections')

# Calling the deserialization for the different formats
def des(deserialization):
    if Config.deserialization_option == "JSON":
        return json.loads(deserialization)
    elif Config.deserialization_option == "BINARY":
        return loads(deserialization)
    elif Config.deserialization_option == "XML":
        return dict2xml(deserialization, wrap="dictionary", indent="  ")
    else:
        print("format not recognised")

# Calling the serialization for the different formats
def ser(serialization):
    if Config.serialization_option == "JSON":
        return json.dumps(serialization)
    elif Config.serialization_option == "BINARY":
        return pickle.dumps(serialization)
    elif Config.serialization_option == "XML":
        return dict2xml(serialization, wrap="dictionary", indent="  ")
    else:
        print("format not recognised")

# Set the options for the encryption of the dictionary
def encrypt():
    f = Fernet(Config.key)
    text = input("GrpC.txt").encode()
    encrypted = f.encrypt(text)
    print("Encrypted dictionary")

# Set the options to print in different formats through the serialization and the deserialization
payload = (Config.Countries)
payload_en = ser(Config.Countries)

# Allows the user to decide over the different output options
Cont = payload
otp = input('Where do you want to print it (1 to console, 2 to a XML, 3 to a TXT encrypted, 4 to a TXT, 5 to a JSON)?: ')
if otp == '1':
    print(payload)
elif otp == '2':
    with open('GrpC.XML', mode='w') as Config.Countries:
        print(payload, file=Config.Countries)
elif otp == '3':
    with open('GrpC_encrypt.txt', mode='w') as Config.Countries:
        print(payload_en, file=Config.Countries)
elif otp == '4':
    with open('GrpC.txt', mode='w') as Config.Countries:
        print(payload, file=Config.Countries)
elif otp == '5':
    with open('GrpC.json', mode='w') as Config.Countries:
        print(payload, file=Config.Countries)
else:
    print('You write an invalid number, please try again')
