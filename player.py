import random

class GameBoard:
    def __init__(self, board):
        self.board = board

    @staticmethod
    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    @staticmethod
    def get_user_input():
        try:
            x_row = input("Enter the row of the ship:")
            while x_row not in '12345678':
                print('Not an appropriate choice, please select a valid row')
                x_row = input("Enter the row of the ship:")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('Not an appropriate choice, please select a valid column')
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        except (ValueError, KeyError):
            print("Not a valid input")
            return Battleship.get_user_input()

    def count_hit_ships(self):
        hit_ships = sum(row.count("X") for row in self.board)
        return hit_ships

def run_game():
    computer_board = GameBoard([[" "] * 8 for _ in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for _ in range(8)])
    Battleship(computer_board.board).create_ships()

    turns = 10
    while turns > 0:
        user_guess_board.print_board()
        user_x_row, user_y_column = Battleship.get_user_input()

        while user_guess_board.board[user_x_row][user_y_column] in {"-", "X"}:
            print("You guessed that one already")
            user_x_row, user_y_column = Battleship.get_user_input()

        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk 1 of my battleships!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed my battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "-"

        if Battleship(user_guess_board.board).count_hit_ships() == 5:
            print("You hit all 5 battleships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("Sorry, you ran out of turns")
                GameBoard(user_guess_board.board).print_board()
                break

if __name__ == '__main__':
    run_game()
