"""This file is for the board class."""
from copy import deepcopy
from os import system

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
        :return: None
        """
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board[i][j], end=" ")
                #import pdb;pdb.set_trace()
            print("")

        return ""

    def refresh(self):
        """
        This function refreshes the screen.
        """
        system("cls")
        print("Welcome to game of 15")
        print(self)

    def move(self, board, empty_location, x, y):
        """
        This function is used for defining a move.
        :param board: 2D array
        :param empty_location: Position in the array
        :param x: int value
        :param y: int value
        :return: Swapped board and updated empty location.
        """
        # check legality of any move
        if empty_location[0] + x < 0 or empty_location[0] + x > 3 or empty_location[1] + y < 0 or empty_location[1] + y > 3:
            return board, empty_location

        # swap
        board[empty_location[0]][empty_location[1]], board[empty_location[0] + x][empty_location[1] + y] \
        = board[empty_location[0] + x][empty_location[1] + y], board[empty_location[0]][empty_location[1]]

        # update empty location
        empty_location[0] += x
        empty_location[1] += y

        return board, empty_location

    def move_up(self, board, empty_location):
        """
        This function is used for move up
        :param board: 2D array
        :param empty_location: Position in the array
        :return: Swapped board and updated empty location.
        """
        return self.move(board, empty_location, -1, 0)

    def move_down(self, board, empty_location):
        """
        This function is used for move down
        :param board: 2D array
        :param empty_location: Position in the array
        :return: Swapped board and updated empty location.
        """
        return self.move(board, empty_location, 1, 0)
    
    def move_left(self, board, empty_location):
        """
        This function is used for move left
        :param board: 2D array
        :param empty_location: Position in the array
        :return: Swapped board and updated empty location.
        """
        return self.move(board, empty_location, 0, -1)

    def move_right(self, board, empty_location):
        """
        This function is used for move right
        :param board: 2D array
        :param empty_location: Position in the array
        :return: Swapped board and updated empty location.
        """
        return self.move(board, empty_location, 0, 1)
