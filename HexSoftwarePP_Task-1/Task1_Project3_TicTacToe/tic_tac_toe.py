import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in win_positions:
        if all(board[pos] == player for pos in combo):
            return True

    return False

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move >= 0 and move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Please enter a number.")

def computer_move():
    available = [i for i in range(9) if board[i] == " "]

    move = random.choice(available)

    board[move] = "O"

def main():
    print("=== Tic Tac Toe ===")

    while True:
        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 You Win!")
            break

        if " " not in board:
            print_board()
            print("🤝 Match Draw!")
            break

        computer_move()

        if check_winner("O"):
            print_board()
            print("💻 Computer Wins!")
            break

        if " " not in board:
            print_board()
            print("🤝 Match Draw!")
            break

if __name__ == "__main__":
    main()