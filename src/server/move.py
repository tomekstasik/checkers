# -*- coding: utf-8 -*-

class Move(object):
    def __init__(self, current_position, destination):
        """Initilize move items - translate to xy"""
        pass

    def translate_to_xy(self, current_position, destination):
        """Translates client move representation to board coordinates:
          A B C D E F G H
        8[               ]8
        7[               ]7
        6[               ]6
        5[               ]5
        4[               ]4
        3[               ]3
        2[               ]2
        1[               ]1
          A B C D E F G H
              row, col
        A8 -> (0,   0), A7 -> (1, 0),... A1 -> (7, 0)
        B8 -> (0, 1),...etc.
        """
        pass

    def get_from(self):
        """Returns from coordinates"""
        pass

    def get_to(self):
        """Returns to coordinates"""
        pass