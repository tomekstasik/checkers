import pytest

from src.server.move import Move

def f():
    m = Move('a', 'b')
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()