def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    """Prints the Tic Tac Toe board to the console."""
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")

def checkWin(xState, zState):
    """Checks if either player has won the game."""
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")

    for i in range(9):  # Loop for a maximum of 9 turns
        printBoard(xState, zState)
        if(turn == 1):
            print("X's Chance")
            while True:
                try:
                    value = int(input("Please enter a value (0-8): "))
                    if 0 <= value <= 8 and xState[value] == 0 and zState[value] == 0:
                        xState[value] = 1
                        break
                    else:
                        print("Invalid move. Please enter a number between 0 and 8 for an empty space.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("O's Chance")
            while True:
                try:
                    value = int(input("Please enter a value (0-8): "))
                    if 0 <= value <= 8 and xState[value] == 0 and zState[value] == 0:
                        zState[value] = 1
                        break
                    else:
                        print("Invalid move. Please enter a number between 0 and 8 for an empty space.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        cwin = checkWin(xState, zState)
        if(cwin != -1):
            printBoard(xState, zState) # Print the final board
            print("Match over")
            break

        turn = 1 - turn

    else: # This else block executes if the loop completes without a break (i.e., no winner)
        printBoard(xState, zState)
        print("It's a draw!")