# -*- coding: utf-8 -*-

from src import Server

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 12345
    LOGFILE = "logs.txt"

    server = Server(HOST, PORT, LOGFILE)
    server.wait_for_players()