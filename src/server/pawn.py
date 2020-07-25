# -*- coding: utf-8 -*-

from pawncolors import PawnColours

class Pawn(object):
    def __init__(self, colour):
        self.colour = colour
        self.king = False

    def make_king(self):
        """Makes current pawn the king"""
        self.king = True

    def __str__(self):
        """Returns string representation of pawn: 'bp' - black pawn, 'wp' - white pawn, 'bk' - black king, 'wk' - white king.
        Usefull for board building when board is sent to client"""
        type = 'p' if not self.king else 'k'
        return self.colour + type
    
    def is_king(self):
        """Returns whether pawn is king or not"""
        return self.king
        

class WhitePawn(Pawn):
    def __init__(self, colour=PawnColours.WHITE):
        super(WhitePawn, self).__init__(colour)


class BlackPawn(Pawn):
    def __init__(self, colour=PawnColours.BLACK):
        super(BlackPawn, self).__init__(colour)