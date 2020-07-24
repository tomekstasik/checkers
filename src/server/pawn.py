# -*- coding: utf-8 -*-

from pawncolors import PawnColors

class Pawn(object):
    def __init__(self, color):
        self.color = color
        self.king = False

    def make_king(self):
        """Makes current pawn the king"""
        self.king = True

    def __str__(self):
        """Returns string representation of pawn: 'bp' - black pawn, 'wp' - white pawn, 'bk' - black king, 'wk' - white king.
        Usefull for board building when board is sent to client"""
        s = 'w' if self.color == PawnColors.WHITE else 'b'
        s += 'p' if not self.king else 'k'
        return s
        

class WhitePawn(Pawn):
    def __init__(self, color=PawnColors.WHITE):
        super(WhitePawn, self).__init__(color)


class BlackPawn(Pawn):
    def __init__(self, color=PawnColors.BLACK):
        super(BlackPawn, self).__init__(color)