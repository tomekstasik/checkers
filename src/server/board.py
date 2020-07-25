# -*- coding: utf-8 -*-

from pawn import (BlackPawn, WhitePawn)
from move import Move

class Board(object):
    def __init__(self, board):
        """Initialize current board"""
        pass

    def generate(self):
        """Generates start board"""
        pass

    def make_move(self, move):
        """Try to make move from current_position to destination"""
        pass

    def is_legal_move(self, move):
        """Checks if current move is leagal"""
        pass

    def is_move_within_board(self, move):
        """Checks if move is within bound of board"""
        pass

    def is_legal_square(self, to):
        """Checks if given destination square is black"""
        pass