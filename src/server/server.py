# -*- coding: utf-8 -*-

from battlethread import BattleThread
from player import Player
from pawncolors import PawnColors

class Server(object):
    """This is server class responsible for waiting for incomming connections."""

    def __init__(self, host, port, battles_history_file):
        """Initialize data for server socket and history file"""
        pass
    
    def wait_for_players(self):
        """When two participans are connected, Player objects need to be created and passed to BattleThread.
        First player - white, second black. Created battle number is following players pair number."""
        pass
    
    def add_battle(self, battle):
        """Adds battle to battles list"""
        pass

    def get_active_battles(self):
        """Returns current battles"""
        pass

    def get_active_players(self):
        """Returns active players list"""
        pass

    def get_battle_info(self, battle_num):
        """Returns battle info by battle number"""
        pass

    def is_nickname_available(self, nickname):
        """Searches active battles list and check used nicknames"""
        pass
