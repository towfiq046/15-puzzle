"""This file is for the board class."""
from copy import deepcopy

# for semantic purpose
MAX_COL = 4
MAX_ROW = 4

class Board:
    """
    Board class which will be the one from where we create new objects.
    """
    def __init__(self):
        self.goal = [
            [" 1", " 2", " 3", " 4"],
            [" 5", " 6", " 7", " 8"],
            [" 9", "10", "11", "12"],
            ["13", "14", "15", "__"]
        ]
        # copying the goal for checking current position is equal to goal or not.
        # copying not referencing.
        self.board = deepcopy(self.goal)    # not self.goal, it will change the goal as both will point the same goal.
        self.empty_location = [MAX_ROW - 1, MAX_COL - 1]

    def __repr__(self):
        """
        It represents the board.
        :return: empty string
        """
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board[i][j], end=" ")
                #import pdb;pdb.set_trace()
            print("")

        return ""
