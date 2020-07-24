# -*- coding: utf-8 -*-

from client import Client

if __name__ == '__main__':
    SERVER_HOST = 'localhost'
    PORT = 12345

    client = Client(SERVER_HOST, PORT)
    client.connect()
    client.enter_nickname()
    client.start_battle()
