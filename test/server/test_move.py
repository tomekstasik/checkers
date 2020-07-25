import pytest

from src.server.move import Move

def test_move_initialization():
    """Checking base Move methods"""
    m = Move('A1', 'B2')
    assert m.get_from_str() == 'A1'
    assert m.get_to_str() == 'B2'
    assert m.get_from_xy() == (7, 0)
    assert m.get_to_xy() == (6, 1)

def test_board_coordinates_toXY():
    """This test is just to check if move coordinates are properly translated to XY coordinates in board table"""
    m = Move()
    for col_num, col_name in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']):
        for row in range(1, 9):
            assert m.translate_to_xy(col_name + str(row)) == (8 - row, col_num)
