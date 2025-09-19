import numpy as np

from typing import Tuple

class Quad:
    """
    Singular game quad that is a 4x4 grid for pieces.

    Holds logic for in-quad movement. This includes:
        - Get/set pieces
        - Flag for passive/aggresive move
        - Checks for valid move
        - Checks for pushing
    """
    def __init__(self):
        #TODO: support emojis
        self.piece1 = "b"
        self.piece2 = "w"
        self.nullpiece = "~"
    
    def __str__(self) -> str:
        ret_str = "\n"
        for row in self.quad:
            for cell in row:
                ret_str += (f"{cell} " if cell != "" else f"{self.nullpiece} ")
            ret_str += "\n"
        return ret_str
    
    def get(self, row: int, col: int) -> str:
        """
        Get piece at position on quad.
        """
        return self.quad[row][col]
    
    def set(self, row: int, col: int, value: str) -> bool:
        """
        Set piece on quad. Return True if successful, else return False.
        """
        if self.quad[row][col] == self.nullpiece or value == self.nullpiece: #override if removing -- i.e., placing a nullpiece
            self.quad[row][col] = value
            return True
        else:
            return False

    def reset_quad(self) -> None:
        """
        Initialize/reset value of a quad.
        """
        self.quad = np.full((4,4), self.nullpiece, dtype=f"U{1}")
        for i in range(4):
            self.quad[0][i] = self.piece2
            self.quad[3][i] = self.piece1
    
    def check_move(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
        """
        Checks to see if move is valid -- i.e., if the end position is at most two consecutive moves away.

        Returns True if move is valid. False if it is not.
        """
        assert start[0] in range(4), f"{start} out of bounds"
        assert start[1] in range(4), f"{start} out of bounds"
        assert end[0] in range(4), f"{end} out of bounds"
        assert end[1] in range(4), f"{end} out of bounds"
        # Two cases: straight line and diagonal
        diff = [end[1] - start[1], end[0] - start[0]]
        if max(diff[0], diff[1]) <= 2:
            if diff[0] == 0 or diff[1] == 0: # check straight line
                return True
            elif sum(diff) <= 2: # check diagonal
                return True
            else:
                return False
        else:
            return False

    def move_piece(self, start: Tuple[int, int], end: Tuple[int, int], first_player: bool = True, passive: bool = True) -> None:
        """
        Take start (row, col) position and move piece to end (row, col) position.
        """
        if self.check_move(start, end):
            #TODO: Check moves only max 2 consecutive spaces
            #TODO: Check that pieces do not intersect or 'push' other pieces on passive move
            #TODO: Implement aggresive move
            self.set(start[0], start[1], self.nullpiece, override=True) # we know this is always filled
            self.set(end[0], end[1], self.piece1 if first_player else self.piece2)
        else:
            raise ValueError(f"Could not move piece from {start} to {end}. Please check if move is valid.")

class Board:
    def __init__(self, num_boards: int = 4):
        assert num_boards % 2 == 0, f"[n={num_boards}] is invalid. Number of boards must be even!"
        self.n = num_boards
    
if __name__=="__main__":
    test = Quad()
    test.reset_quad()
    print(test)
    test.move_piece((3, 0), (2, 1), True)

    print(test)
    # test.move_piece((0,0), (1, 2), False) # This is an invalid move!
    test.move_piece((0, 0), (2, 0), False) # TODO: This case is failing....
    print(test)
    test.reset_quad()
    print(test)
