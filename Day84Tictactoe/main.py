import random

print("Tic Tac Toe Game")
print("----------------")

possiblenumbers = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
columns = 3

def GameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(columns):
            print("", board[x][y], end=" |")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    if(num == 0):
        board[0][0] = turn
    elif(num == 1):
        board[0][1] = turn
    elif(num == 2):
        board[0][2] = turn
    elif(num == 3):
        board[1][0] = turn
    elif(num == 4):
        board[1][1] = turn
    elif(num == 5):
        board[1][2] = turn
    elif(num == 6):
        board[2][0] = turn
    elif(num == 7):
        board[2][1] = turn
    elif(num == 8):
        board[2][2] = turn
def checkwinner(board):
    ### X axis
    if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        print("O has won!")
        return "O"
    elif (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        print("X has won!")
        return "X"
    elif (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        print("O has won!")
        return "O"
    elif (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Y axis
    if (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        print("O has won!")
        return "O"
    elif (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        print("X has won!")
        return "X"
    elif (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Cross wins
    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
    elif (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        print("O has won!")
        return "O"
    else:
        return "N"
Is_on = False

turncount = 0

while(Is_on == False):
    if(turncount % 2 == 1):
        print(GameBoard())
        numberpick = int(input("\n Choose a number between [1-9]: "))
        if numberpick in possiblenumbers:
            modifyArray(numberpick,'X')
            possiblenumbers.remove(numberpick)
            turncount += 1
            winner = checkwinner(board)
            if(winner != "N"):
                print(GameBoard())
                print("\nGame over!")
                break
        else:
            print("Invalid input. Try another number.")
            continue
    else:
        if not possiblenumbers:
            print("\nIt's a tie!")
            break
        while(True):
            cpuChoice = random.choice(possiblenumbers)
            print("\n Cpu choice: ", cpuChoice)
            if(cpuChoice in possiblenumbers):
                modifyArray(cpuChoice, 'O')
                possiblenumbers.remove(cpuChoice)
                turncount += 1
                break
        winner = checkwinner(board)
        if(winner != "N"):
            print("\nGame over!")
            break