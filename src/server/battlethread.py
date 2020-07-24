# -*- coding: utf-8 -*-

import threading
import json
from datetime import datetime

class BattleThread(threading.Thread):
    """This class describes thread created after two participants connect to the server to start the game"""
    def __init__(self, player_a, player_b, battle_num):
        """Stores players and battle number"""
        pass
    
    def run(self):
        """Start battle thread, white player makes very first move"""
        pass
    
    def do_move(self, player, move):
        """Makes move for player"""
        pass

    def get_opponent(self, player):
        """Return current player opponent - usefull to assign next turn"""
        pass

    def get_players_nicknames(self):
        """Return players nicknames for current battle"""
        pass

    def set_start_date(self):
        """Sets battle start date/time"""
        pass

    def get_start_date(self):
        """Returns battle start date/time"""
        pass

    def set_end_date(self):
        """Sets battle end date/time"""
        pass

    def get_end_date(self):
        """Returns battle end date/time"""
        pass

    def send_board(self, board):
        """Sends current board state to clients - jsonified board, like [['bp', 'bp', None,...],[...],[None, 'wp', 'wk'...]] etc."""
        pass
