from core.othello import Othello, State
from core.ui import print_board, user_move, print_score, print_turn
from core.mcts import _random_move
from core.minimax import minimax_move


def main():
    print("Welcome to Othello!")
    
    game = Othello()
    round = 0
    while game.state == State.BLACK_TURN or game.state == State.WHITE_TURN:
        round += 1
        print(f"\n      Round {round}")
        print_board(game.board)
        print_score(game)
        try:
            x, y = minimax_move(game, 4) if game.state == State.WHITE_TURN else _random_move(game)
            print_turn(game)
            print(f"move: {chr(ord('A') + x)}{str(y + 1)}")
            game.make_move(x, y)
        except IndexError as e:
            print(e)

    print(f"\n      Game Over")
    print_board(game.board)
    print_score(game)
    if game.state == State.BLACK_WON:
        print("\nBlack won!\n")
    elif game.state == State.WHITE_WON:
        print("\nWhite won!\n")
    else:
        print("\nDraw!\n")


if __name__ == "__main__":
    main()