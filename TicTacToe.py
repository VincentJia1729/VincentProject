
# Tic-tac-toe

import random

'''
Your program should keep looping until the game ends (either one player wins or
the game ends in a draw).
• Ask the human player for enter a valid coordinate to place an ”X”. Reprompt
them until a valid unused coordinate is supplied. Update the board to reflect the
user input.
• Check if the game has ended. If exit, print out the final state of the board, and
print a statement indicating the result (player win or was it a draw).


• If the game has not ended, print the new state of the board.
• Continue to generate a random valid move for the computer player. Update the
board to reflect the computer’s choice.
• Check if the game has ended. If exit, print out the final state of the board, and
print a statement indicating the result (computer win or was it a draw).
• Repeat until the game ends.
'''


board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]


    
def printBoard(L):
    '''
    (list) --> none
    I: a list L
    P: prints L's rows and columns
    O: A print statement of the list L
    '''
    
    for row in L:
        for col in row:
            print(col, end = " ")
        print()
    print()

def enterPlayerX(string):
    '''
    (string) --> none
    I: input a string chose the place to put the player X
    P: cuts string into two parts. Changes list based on given row and col to 'X'
    O: Changes list based on given row and col to 'X'
    '''
    row = int(string[0])
    col = int(string[2])
    board[row][col] = "X"

def enterComputerO(row, col):
    '''
    (int, int) --> none
    I: input two ints
    P: Changes list based on given row and col to 'O'
    O: Changes list based on given row and col to 'O'
    '''
    board[row][col] = "O"
    
def isValidMove(L, row, col):
    '''
    (list, int, int) --> bool
    I: List, int, int
    P: Checks if position is a valid move. row and col have to be within 0-2 inclusive and be in a space with '.' 
    O: True or False
    '''
    return row >= 0 and row <= 2 and \
           col >= 0 and col <= 2 and \
           board[row][col] == '.'

def checkRow(L, row, ch):
    '''
    (list, int, chr) --> bool
    I: List, int, chr
    P: Checks if any player has won by matching 3 in a row
    O: True or False
    '''
    result = True
    for col in L[row]:
        result = result and (col == ch)
    return result

def checkCol(L, col, ch):
    '''
    (list, int, chr) --> bool
    I: List, int, chr
    P: Checks if any player has won by matching 3 in a col
    O: True or False
    '''
    result = True
    for i in range(3):
        result = result and (L[i][col] == ch)
    return result

def checkDiagonal(L,ch):
    '''
    (list, chr) --> bool
    I: List, chr
    P: Checks if any player has won by matching 3 in a diagonal
    O: True or False
    '''
    result1 = True
    result2 = True

    for i in range(3):
        result1 = result1 and (L[i][i] == ch)
        result2 = result2 and (L[i][3-i-1] == ch)

    return result1 or result2

def hasWon(L, ch):
    '''
    (list, chr) --> bool
    I: List, chr
    P: checks if any player has won using checkRow(), checkCol() and checkDiagonal()
    O: True or False
    '''
    
    return checkRow(L, 0, ch) or \
           checkRow(L, 1, ch) or \
           checkRow(L, 2, ch) or \
           checkCol(L, 0, ch) or \
           checkCol(L, 1, ch) or \
           checkCol(L, 2, ch) or \
           checkDiagonal(L,ch)

def isDraw(L):
    '''
    (list) --> bool
    I: List
    P: checks if is draw if all spaces are filled 
    O: True or False
    '''
    for row in L:
        for col in row:
            if col == ".":
                return False
    return True

def isGameOver(L):
    '''
    (list) --> bool
    I: List
    P: Checks if anyplayer has won
    O: True or False
    '''
    return hasWon(L, "X") or hasWon(L, "O") or isDraw(L)
    

def playTicTacToe(board):
    '''
    (list) --> none
    I: list
    P: plays TicTacToe (the human player goes first)
    O: none
    '''

    while not isGameOver(board):

        # player turn
        
        inp = input("Player, enter an X position in the form n,n: ")
        row = int(inp[0])
        col = int(inp[2])
        while not isValidMove(board, row, col):
            inp = input("Player, enter an X position in the form n,n: ")
            row = int(inp[0])
            col = int(inp[2])

        else:
            enterPlayerX(inp)
            printBoard(board)
            
        if isGameOver(board) == True:
            break

        # computer turn

        row = random.randint(0,2)
        col = random.randint(0,2)
        
        while not isValidMove(board, row, col):
            row = random.randint(0,2)
            col = random.randint(0,2)

        else:
            enterComputerO(row, col)
            printBoard(board)


    if hasWon(board, "X"):
        print("Player has won")

    elif hasWon(board, "O"):
        print("Computer has won")

    elif isDraw(board):
        print("Is draw")

# play game

uno = playTicTacToe(board)
    

    
        



    


            





















