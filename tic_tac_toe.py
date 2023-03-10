import time

#Set up

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

currentPlayer = "X"
gameRunning = True
winner = "None"
x_score = 0
o_score = 0

#Board print

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print((board[6] + " | " + board[7] + " | " + board[8]))

#Player input + switch

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    elif inp > 9:
        print("Enter a valid number")
    else:
        print("The tile is already occupied")

def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
        if gameRunning: 
            print("O's move")
    else:
        currentPlayer = "X"
        if gameRunning:
            print("X's move")

#Win conditions

def checkWin(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
    elif (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
    elif (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
    else:
        return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        print("Its a tie!")
        gameRunning = False

def checkWinner(board):
    global gameRunning
    global currentPlayer
    global winner
    if checkWin(board):
        print("The winner is " + currentPlayer)
        winner = currentPlayer
        gameRunning = False

#Scoreboard

def addPoints(board):
    global winner
    global o_score
    global x_score
    if winner == "X":
        x_score += 1
    if winner == "O":
        o_score += 1

def showScore(board):
    print("Score is {0} - {1}".format(x_score, o_score))
    if x_score > o_score:
        print("X is leading by " + str(x_score - o_score))
    elif o_score > x_score:
        print("O is leading by " + str(o_score - x_score))
    else:
        print("The score is tied")   

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    checkWin(board)
    checkWinner(board)
    addPoints(board)
    switchPlayer(board)
    
    if not gameRunning:
        showScore(board)
        playAgain = input("Do you want to play again? (yes/no)")
        if playAgain.lower() == "yes" or playAgain.lower() == "y":
            board = ["-", "-", "-",
                     "-", "-", "-",
                     "-", "-", "-"]
            currentPlayer = "X"
            gameRunning = True
            winner = "None"
        elif playAgain.lower() == "no" or playAgain.lower() == "n":
            print("Thanks for playing!")
            time.sleep(3)
            gameRunning = False
        else: 
            print("Please input valid value")