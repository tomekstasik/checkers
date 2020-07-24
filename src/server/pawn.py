# -*- coding: utf-8 -*-

from pawncolors import PawnColors

class Pawn:
    def __init__(self, color):
        self.color = color
        self.king = False

    def make_king(self):
        """Makes current pawn the king"""
        self.king = True


class WhitePawn(Pawn):
    def __init__(self, color=PawnColors.WHITE):
        super().__init__(color)


class BlackPawn(Pawn):
    def __init__(self, color=PawnColors.BLACK):
        super().__init__(color)