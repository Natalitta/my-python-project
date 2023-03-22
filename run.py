from random import randint

scores = {"robot": 0, "user": 0}

class Board:
    """
    Creates the board, its size, type (robot or user's board).
    Player's name.
    """
    def __init__(self, size, ships_number, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.ships_number = ships_number
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "x"

        if (x, y) in self.ships:
            self.board[x][y] ="*"
            return "yes"
        else:
            return "no"

        
    def add_ship(self, x, y, type="robot"):
        if len(self.ships) >= self.ships_number:
            print("Sorry, no more ships can be added")
        else:
            self.ships.append((x, y))
            if self.type == "user":
                self.board[x][y] = "&"


def random(size):
    """
    It helps to return a random number (0 - size)
    """
    return radint (0, size - 1)


def validate(x, y, board):


def populate_board(board):


def make_guess(board):


def play_game(robot_board, user_board):


def new_game:
    """
    It begins the game from the start. 
    New boards, zero score.
    """
    size = 6
    ships_number = 5
    scores["robot"] = 0
    scores["user"] = 0
    print("-" * 35)
    print("Welcome to the Battleships game!")
    print(f"Your board size: {size}. You have {ships_number} ships.")
    print("Coordinates start in the left top corner (row: 0, column: 0)")


