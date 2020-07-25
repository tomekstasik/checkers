# -*- coding: utf-8 -*-

class Move(object):

    def __init__(self, str_from=None, str_to=None):
        """Initilize move items - translate to xy"""
        pass

    def translate_to_xy(self, str_coord):
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
        A1  =  (7, 0)
        A2  =  (6, 0)
        A3  =  (5, 0)
        A4  =  (4, 0)
        A5  =  (3, 0)
        A6  =  (2, 0)
        A7  =  (1, 0)
        A8  =  (0, 0), etc.
        """
        pass

    def get_from_xy(self):
        """Returns 'from' coordinates"""
        pass

    def get_from_str(self):
        """Returns string like 'from' coordinates, eg. A1, B4, etc."""
        pass

    def get_to_xy(self):
        """Returns 'to' coordinates"""
        pass

    def get_to_str(self):
        """Returns string like 'to' coordinates, eg. A1, B4, etc."""
        pass
