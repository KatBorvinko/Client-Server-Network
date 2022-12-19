import unittest
import socket

import Config


class Test_connection(unittest.TestCase):
    def test(self):
        client_socket = socket.socket()
        client_socket.connect(('local host', Config.port_number))
        client_socket.send('message1'.encode())
        self.assertEqual(client_socket.recv(1024).decode(), 'message1')
        client_socket.close()


if __name__ == '__main__':
    unittest.main()
