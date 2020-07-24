# -*- coding: utf-8 -*-

class Client(object):
    def __init__(self, server_host, port):
        """Stores data about server connection"""
        pass

    def connect(self):
        """Creates socket and establishes connection with game server"""
        pass

    def enter_nickname(self):
        """Reads nickname from standard input and sends to game server.
        It's done until server returns info nickname is available"""
        pass

    def start_battle(self):
        """Starts new battle"""
        pass

    def draw_board(self, board):
        """Draws current board state """
        pass

    def enter_move(self):
        """Reads next move data from standard input and sends to game server"""
        pass
