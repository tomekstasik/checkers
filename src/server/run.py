# -*- coding: utf-8 -*-

from server import Server

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 12345
    HISTORY_FILE = "battles_history.txt"

    server = Server(HOST, PORT, HISTORY_FILE)
    server.wait_for_players()