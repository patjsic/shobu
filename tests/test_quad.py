import pytest

from src.board import Quad

def test_diagonal_linear():
    test = Quad()
    test.reset_quad()
    test.move_piece((3, 0), (2, 1), True)

    test.move_piece((0, 0), (2, 0), False)
    test.move_piece((0, 0), (2, 0), False)
    test.move_piece((0, 0), (2, 0), False)
    test.move_piece((3, 1), (1, 3), True)

    with pytest.raises(ValueError):
        test.move_piece((1, 3), (3, 0), True)  # This should fail
    test.move_piece((0, 0), (2, 0), False)
    test.move_piece((0, 0), (5, 0), False) #This doesn't fail because there is no piece being moved.

    with pytest.raises(ValueError):
        test.move_piece((3, 3), (0, 0), True) # This should fail since it moves diagonal > 2 spaces
    test.reset_quad()