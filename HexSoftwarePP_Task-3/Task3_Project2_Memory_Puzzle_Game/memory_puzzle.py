import random
import time

# Create card pairs
cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
random.shuffle(cards)

board = ['*'] * 8
matched = [False] * 8

moves = 0
start_time = time.time()

def display_board():
    print("\nBoard:")
    for i in range(8):
        print(board[i], end=" ")
        if (i + 1) % 4 == 0:
            print()

def display_positions():
    print("\nPositions:")
    for i in range(1, 9):
        print(i, end=" ")
        if i % 4 == 0:
            print()

print("===== MEMORY PUZZLE GAME =====")

display_positions()

while not all(matched):

    display_board()

    try:
        pos1 = int(input("\nEnter first position (1-8): ")) - 1
        pos2 = int(input("Enter second position (1-8): ")) - 1

        if pos1 == pos2:
            print("Choose different positions!")
            continue

        if matched[pos1] or matched[pos2]:
            print("Position already matched!")
            continue

        board[pos1] = cards[pos1]
        board[pos2] = cards[pos2]

        display_board()

        moves += 1

        if cards[pos1] == cards[pos2]:
            print("\n✅ Match Found!")

            matched[pos1] = True
            matched[pos2] = True

        else:
            print("\n❌ Not a Match!")

            time.sleep(2)

            board[pos1] = '*'
            board[pos2] = '*'

    except:
        print("Invalid Input!")

end_time = time.time()

print("\n🎉 Congratulations!")
print("You matched all pairs.")

print(f"Total Moves: {moves}")
print(f"Time Taken: {round(end_time - start_time, 2)} seconds")