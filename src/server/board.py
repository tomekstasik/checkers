# -*- coding: utf-8 -*-

from pawn import (BlackPawn, WhitePawn)
from move import Move

class Board(object):
    SIZE = 8 # means 8x8

    def __init__(self, board=None):
        """Initialize current board"""
        pass

    @staticmethod
    def generate():
        """Generates start board"""
        pass

    def make_move(self, move):
        """Try to make move from current_position to destination, returns True if move passed, false otherwise"""
        pass

    def is_legal_move(self, move):
        """Checks if current move is leagal"""
        pass

    def is_move_within_board(self, move):
        """Checks if move is within bound of board"""
        pass

    def is_black_square(self, to):
        """Checks if given destination square is black"""
        pass

    def get_board(self):
        """Return current boart state"""
        pass