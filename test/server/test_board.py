# -*- coding: utf-8 -*-

import pytest

from src.server.board import Board
from src.server.pawn import (BlackPawn, WhitePawn)
from src.server.move import Move

def test_initial_board_generation():
    """Below should be generated:
        [
            0 [None, BlackPawn(), None, BlackPawn(), None, BlackPawn(), None, BlackPawn()],
            1 [BlackPawn(), None, BlackPawn(), None, BlackPawn(), None, BlackPawn(), None],
            2 [None, BlackPawn(), None, BlackPawn(), None, BlackPawn(), None, BlackPawn()],
            3 [None, None,        None, None,        None, None,        None,        None],
            4 [None, None,        None, None,        None, None,        None,        None],
            5 [WhitePawn(), None, WhitePawn(), None, WhitePawn(), None, WhitePawn(), None],
            6 [None, WhitePawn(), None, WhitePawn(), None, WhitePawn(), None, WhitePawn()],
            7 [WhitePawn(), None, WhitePawn(), None, WhitePawn(), None, WhitePawn(), None]
        ]"""

    board = Board.generate()

    ### First & third row (top)
    for row_num in [0, 2]:
        # Check white fields
        for f in [0, 2, 4, 6]:
            assert board[row_num][f] is None
        # Check black fields
        for f in [1, 3, 5, 7]:
            assert isinstance(board[row_num][f], BlackPawn)
    ### Second row with black pawns
    # Check white fields
    for f in [1, 3, 5, 7]:
        assert board[1][f] is None
    # Check black fields
    for f in [0, 2, 4, 6]:
        assert isinstance(board[1][f], BlackPawn)
    ### Middle of the board - all none
    for row_num in [3, 4]:
        for f in range(0, 8):
            assert board[row_num][f] is None
    
    ### Bottom of board
    for row_num in [5, 7]:
        # Check white fields
        for f in [1, 3, 5, 7]:
            assert board[row_num][f] is None
        # Check black fields
        for f in [0, 2, 4, 6]:
            assert isinstance(board[row_num][f], WhitePawn)
    ### Row # 6
    for f in [1, 3, 5, 7]:
        assert isinstance(board[6][f], WhitePawn)

def test_is_back_square():
    board = Board()
    for f in ['A7', 'A5', 'A3', 'A1',
              'C7', 'C5', 'C3', 'C1',
              'E7', 'E5', 'E3', 'E1',
              'G7', 'G5', 'G3', 'G1',
              'B8', 'B6', 'B4', 'B2',
              'D8', 'D6', 'D4', 'D2',
              'F8', 'F6', 'F4', 'F2',
              'H8', 'H6', 'H4', 'H2']:
        assert board.is_black_square(f) is True
    for f in ['A8', 'A6', 'A4', 'A2',
            'C8', 'C6', 'C4', 'C2',
            'E8', 'E6', 'E4', 'E2',
            'G8', 'G6', 'G4', 'G2',
            'B7', 'B5', 'B3', 'B1',
            'D7', 'D5', 'D3', 'D1',
            'F7', 'F5', 'F3', 'F1',
            'H7', 'H5', 'H3', 'H1']:
        assert board.is_black_square(f) is False

def test_do_not_move_to_white_square():
    """It actually tests is_black_square()"""
    black_pawn = BlackPawn()
    # Lets use smaller board - full size is not required here
    board = [ # Left upper corner of board
        [None, black_pawn],
        [None,       None]
    ]
    gameboard = Board(board)
    # Let's try to move from B8 to B7
    move = Move('B8', 'B7')
    result = gameboard.make_move(move)
    assert result is False
    assert gameboard.get_board() == board

def test_do_not_move_out_of_board():
    black_pawn = BlackPawn()
    # Lets use smaller board - full size is not required here
    board = [ # Left upper corner of board
        [None, black_pawn],
        [None,       None]
    ]
    gameboard = Board(board)
    move = Move('B8', 'B9')
    result = gameboard.is_move_within_board(move)
    assert result is False

    result = gameboard.make_move(move)
    assert result is False
    assert gameboard.get_board() == board

def test_move_black_pawn_one_field_down():
    black_pawn = BlackPawn()
    # Lets use smaller board - full size is not required here
    board = [ # Left upper corner of board
        [None, black_pawn],
        [None,       None]
    ]
    gameboard = Board(board)
    move = Move('B8', 'A7')
    result = gameboard.is_move_within_board(move)
    assert result is True

    result = gameboard.make_move(move)
    assert result is True
    assert gameboard.get_board() == [
        [None,       None],
        [black_pawn, None]
    ]

def test_do_not_move_black_pawn_up_back():
    black_pawn = BlackPawn()
    board = [ # Left upper corner of board
        [None,      None],
        [black_pawn, None]
    ]
    gameboard = Board(board)
    move = Move('A7', 'B8')
    result = gameboard.make_move(move)
    assert result is False
    gameboard.get_board() == board

def test_move_white_pawn_up():
    white_pawn = WhitePawn()
    board = [ # let assume left bottom corner of board
        [None,       None], #8
        [None,       None], #7
        [None,       None], #6
        [None,       None], #5
        [None,       None], #4
        [None,       None], #3
        [None,       None], #2
        [white_pawn, None], #1
    ]
    gameboard = Board(board)
    move = Move('A1', 'B2')
    result = gameboard.is_move_within_board(move)
    assert result is True

    result = gameboard.make_move(move)
    assert result is True
    assert gameboard.get_board() == [
        [None,       None], #8
        [None,       None], #7
        [None,       None], #6
        [None,       None], #5
        [None,       None], #4
        [None,       None], #3
        [None, white_pawn], #2
        [None,       None], #1
    ]

def test_do_not_move_white_pawn_down_back():
    white_pawn = WhitePawn()
    board = [ # let assume left bottom corner of board
        # A           B
        [None,       None], #8
        [None,       None], #7
        [None,       None], #6
        [None,       None], #5
        [None,       None], #4
        [None,       None], #3
        [None, white_pawn], #2
        [None,       None], #1
    ]
    gameboard = Board(board)
    move = Move('B2', 'A1')
    result = gameboard.make_move(move)
    assert result is False
    assert gameboard.get_board() == board

def test_do_not_move_black_pawn_onto_white():
    white_pawn = WhitePawn()
    black_pawn = BlackPawn()
    board = [ # Left upper corner of board
        [None, black_pawn],
        [white_pawn, None],
    ]
    gameboard = Board(board)
    move = Move('B8', 'A7')
    result = gameboard.make_move(move)
    assert result is False
    assert gameboard.get_board() == board

def test_do_not_move_white_pawn_onto_black():
    white_pawn = WhitePawn()
    black_pawn = BlackPawn()
    board = [ # Left upper corner of board
        [None, black_pawn],
        [white_pawn, None],
    ]
    gameboard = Board(board)
    move = Move('A7', 'B8')
    result = gameboard.make_move(move)
    assert result is False
    assert gameboard.get_board() == board

def test_do_not_move_pawn_more_than_one_square():
    dark_pawn =  BlackPawn()
    board = [ # Left upper corner
        # A     B          C     D
        [None, dark_pawn, None, None],
        [None, None,      None, None],
        [None, None,      None, None],
        [None, None,      None, None]
    ]
    gameboard = Board(board)
    move = Move('B8', 'D6')
    result = gameboard.make_move(move)
    assert result is False
    assert gameboard.get_board() == board

def test_black_captures_white():
    white_pawn = WhitePawn()
    black_pawn = BlackPawn()
    board = [
        # A     B           C     D
        [None, black_pawn, None, None], # 8
        [None, None, white_pawn, None], # 7
        [None, None,       None, None], # 6
        [None, None,       None, None]  # 5
    ]
    gameboard = Board(board)
    move = Move('B8', 'D6')
    result = gameboard.make_move(move)
    assert result is True
    assert gameboard.get_board() == [
        # A     B           C     D
        [None, None, None, None], # 8
        [None, None, None, None], # 7
        [None, None, None, black_pawn], # 6
        [None, None, None, None]  # 5
    ]

def test_white_captures_black():
    white_pawn = WhitePawn()
    black_pawn = BlackPawn()
    board = [
        [None,       None, None, None], # 8
        [None,       None, None, None], # 7
        [None,       None, None, None], # 6
        [None,       None, None, None], # 5
        [None,       None, None, None], # 4
        [None,       None, None, None], # 3
        [None, black_pawn, None, None], # 2
        [white_pawn, None, None, None]  # 1
        # A           B     C     D
    ]
    gameboard = Board(board)
    move = Move('A1', 'C3')
    result = gameboard.make_move(move)
    assert result is True
    assert gameboard.get_board() ==  [
        [None, None, None, None], # 8
        [None, None, None, None], # 7
        [None, None, None, None], # 6
        [None, None, None, None], # 5
        [None, None, None, None], # 4
        [None, None, white_pawn, None], # 3
        [None, None, None, None], # 2
        [None, None, None, None] # 1
        # A      B     C     D
    ]

def test_black_pawn_becomes_king():
    black_pawn = BlackPawn()
    board = [
        [None,       None], # 8
        [None,       None], # 7
        [None,       None], # 6
        [None,       None], # 5
        [None,       None], # 4
        [None,       None], # 3
        [None, black_pawn], # 2
        [None,       None], # 1
        # A           B
    ]
    gameboard = Board(board)
    move = Move('B2', 'A1')
    result = gameboard.make_move(move)
    assert result is True
    assert black_pawn.is_king() is True
    assert gameboard.get_board() == [
        [None,       None], # 8
        [None,       None], # 7
        [None,       None], # 6
        [None,       None], # 5
        [None,       None], # 4
        [None,       None], # 3
        [None,       None], # 2
        [black_pawn, None], # 1
        # A           B
    ]

def test_white_pawn_becomes_king():
    white_pawn = WhitePawn()
    board = [
        # A           B
        [None,       None], # 8
        [white_pawn, None], # 7
    ]
    gameboard = Board(board)
    move = Move('A7', 'B8')
    result = gameboard.make_move(move)
    assert result is True
    assert white_pawn.is_king() is True
    assert gameboard.get_board() == [
        # A      B
        [None, white_pawn], # 8
        [None,       None], # 7
    ]
# and so on...
# TODO: more tests for kings logic

def test_get_board_for_ascii():
    """Checks if board is converted properly to format which can be easily converted to JSON"""
    board = [
            [None, BlackPawn(), None, BlackPawn(), None, BlackPawn(), None, BlackPawn()],
            [BlackPawn(), None, BlackPawn(), None, BlackPawn(), None, BlackPawn(), None],
            [None, BlackPawn(), None, BlackPawn(), None, BlackPawn(), None, BlackPawn()],
            [None, None,        None, None,        None, None,        None,        None],
            [None, None,        None, None,        None, None,        None,        None],
            [WhitePawn(), None, WhitePawn(), None, WhitePawn(), None, WhitePawn(), None],
            [None, WhitePawn(), None, WhitePawn(), None, WhitePawn(), None, WhitePawn()],
            [WhitePawn(), None, WhitePawn(), None, WhitePawn(), None, WhitePawn(), None]
        ]
    gameboard = Board(board)
    assert gameboard.get_board_for_ascii() == [
            [None, 'bp', None, 'bp', None, 'bp', None, 'bp'],
            ['bp', None, 'bp', None, 'bp', None, 'bp', None],
            [None, 'bp', None, 'bp', None, 'bp', None, 'bp'],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['wp', None, 'wp', None, 'wp', None, 'wp', None],
            [None, 'wp', None, 'wp', None, 'wp', None, 'wp'],
            ['wp', None, 'wp', None, 'wp', None, 'wp', None]
    ]
    bk = BlackPawn()
    bk.make_king()
    wk = WhitePawn()
    wk.make_king()

    board = [
        [None, bk, None, BlackPawn(), None, BlackPawn(), None, BlackPawn()],
        [WhitePawn(), None, wk, None, WhitePawn(), None, WhitePawn(), None]
    ]
    gameboard = Board(board)
    assert gameboard.get_board_for_ascii() == [
        [None, 'bk', None, 'bp', None, 'bp', None, 'bp'],
        ['wp', None, 'wk', None, 'wp', None, 'wp', None]
    ]