"""This file is for the board class."""
from copy import deepcopy
from os import system
from queue import Queue
from random import randint, seed

# for semantic purpose
MAX_COL = 4
MAX_ROW = 4
SHUFFLE = 20

class Board:
    """Models the board."""

    def __init__(self):
        """Construct a board"""

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
        self.moves = {0: self.move_up, 1: self.move_down, 2: self.move_left, 3: self.move_right}

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
        """This function refreshes the screen."""

        system("cls")
        print("Welcome to game of 15")
        print(self)

        if self.goal == self.board:
            print("\nCongrats! you've won.")
            return False
        return True

    def shuffle(self):
        """Shuffles the board from the start."""
        seed()
        for i in range(SHUFFLE):
            m = randint(0, 3)
            self.moves[m](self.board, self.empty_location )

        # Move the empty location at bottom right.
        for i in range(MAX_COL):
            self.moves[1](self.board, self.empty_location)

        for i in range(MAX_ROW):
            self.moves[3](self.board, self.empty_location)

    def solve(self):
        """solves the game using BFS"""
        def successors(board, empty_location):
            board_list = [deepcopy(board), deepcopy(board), deepcopy(board), deepcopy(board)]   # up down ..
            empty_location_list = [list(empty_location), list(empty_location), list(empty_location), list(empty_location)]

            board_list[0], empty_location_list[0] = self.move_up(board_list[0], empty_location_list[0])
            board_list[1], empty_location_list[1] = self.move_down(board_list[1], empty_location_list[1])
            board_list[2], empty_location_list[2] = self.move_left(board_list[2], empty_location_list[2])
            board_list[3], empty_location_list[3] = self.move_right(board_list[3], empty_location_list[3])

            return [[board_list[0], empty_location_list[0], 0], [board_list[1], empty_location_list[1], 1], \
                [board_list[2], empty_location_list[2], 2], [board_list[3], empty_location_list[3], 3]]

        # Keeping track of the board state.
        searched = set()
        fringe = Queue()    # next moves in queue.
        
        fringe.put({"board": self.board, "empty_location": self.empty_location, "path": [] })

        while True:
            # Quit if no solution is found
            if fringe.empty():
                return []
            
            # Inspect current node
            node = fringe.get()

            if node["board"] == self.goal:
                return node["path"]
            
            # Add current node to searched set: put children in fringe.
            if str(node["board"]) not in searched:
                searched.add(str(node["board"]))
                for child in successors(node["board"], node["empty_location"]):
                    if str(child[0]) not in searched:
                        fringe.put({"board": child[0], "empty_location": child[1], "path": node["path"] + [child[2]]})



    def move(self, board, empty_location, x, y):
        """
        This function is used for making a legal move.
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
        """This function is used for move down"""
        return self.move(board, empty_location, 1, 0)
    
    def move_left(self, board, empty_location):
        """This function is used for move left"""
        return self.move(board, empty_location, 0, -1)

    def move_right(self, board, empty_location):
        """This function is used for move right"""
        return self.move(board, empty_location, 0, 1)

