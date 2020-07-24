# -*- coding: utf-8 -*-

import threading
from datetime import datetime

class BattleThread(threading.Thread):
    """This class describes thread created after two participants connect to the server to start the game"""
    def __init__(self, player_a, player_b):
        """Stores players list, sets """
        pass
    
    def run(self):
        """Start battle thread"""
        pass
    
    def do_move(self, player, move):
        """Makes move for player"""
        pass

    def get_players_info(self):
        """Return players data for current battle"""
        pass

    def set_start_date(self):
        """Sets battle start date/time"""
        pass

    def set_end_date(self):
        """Sets battle end date/time"""
        pass