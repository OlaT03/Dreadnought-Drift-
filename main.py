# main.py
from computer import Player
from computer import Computer

def main():
    board_size = 8  
    player = Player("Player 1", board_size)
    computer = Computer(board_size)

    player.place_ships()
    computer.place_ships()

    while not player.board.is_game_over() and not computer.board.is_game_over():
        player.make_move(computer.board)
        computer.make_move(player.board)

    print("Game Over!")

if __name__ == "__main__":
    main()
