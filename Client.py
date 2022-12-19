import json
import pickle
import dict2xml as dict2xml
import Config
import socket
from dict2xml import dict2xml
from cryptography.fernet import Fernet

COUNTRIES = Config.countries


# Server connection
def connect_to_server():
    client = socket.socket()
    client.connect((Config.server_address, Config.port_number))
    name = input("Enter your name, please: ")
    client.send(bytes(name, 'utf-8'))
    data = input("Please type dictionary: ")
    client.send(bytes(data, 'utf-8'))
    print("Welcome to the dictionary:")

    if __name__ == '__main__':
        connect_to_server()

    for key, value in COUNTRIES.items():
        print(key, value)


# Edit dictionary
def edit(self, key, value):
    self.dictionary[key] = value


# Serialization/ pickle file
def serialise_dictionary(self):
    if Config.serialization_option == "JSON":
        with open('dico.json', 'w') as f:
            json.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: JSON')
    elif Config.serialization_option == "BINARY":
        with open('dico.bin', 'wb') as f:
            pickle.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: Binary')
    elif Config.serialization_option == "XML":
        xml_content = dict2xml(self.dictionary, wrap="dictionary", indent="  ")
        with open('dico.xml', 'w') as f:
            f.write(xml_content)
            f.close()
            print('Dictionary serialised as XML. Filename: xml')


# File encryption
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
