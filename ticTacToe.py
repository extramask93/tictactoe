import random

def rollPlayer():
    r = random.randint(0,1)
    if(r==1):
        return 'player'
    else:
        return 'computer'
    
def chooseSide():
    letter=''
    while(letter!='X' and letter!='O'):
        print('Choose your side! Type X or O to proceed')
        letter=input().upper()
    if(letter=='X'):
        return ['X','O']
    else:
        return ['O','X']
    
def isWinner(board,letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
    (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
    (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
    (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
    (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
    (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal
def getMove(board):
    while(True):
           print('Enter your move: ')
           try:
               move=int(input());
           except ValueError:
                continue
           if(move in range(1,10) and isFree(board,move)):
                return move
def isFree(board, move):
    return board[move]==' '
def isBoardFull(board):
    for i in range(1,10):
        if(isFree(board,i)):
            return False
    return True
      
def makeMove(board, playerLetter, move):
    board[move]=playerLetter;
def printBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def play():
    Board = [' ']*10;
    playerLetter,computerLetter = chooseSide()
    turn=rollPlayer()
    print(turn +' begins')
    for i in range(9):
        if(turn=='player'):
            printBoard(Board)
            move=getMove(Board)
            makeMove(Board,playerLetter,move)
            if(isWinner(Board,playerLetter)):
                print('Player '+ turn + ' wins!')
                break
            else:
                if(isBoardFull(Board)):
                    print('The game is a tie!')
                    return
                
        if(turn=='computer'):
            printBoard(Board)
            move=getMove(Board)
            makeMove(Board,computerLetter,move)
            if(isWinner(Board,computerLetter)):
                print('Player '+ turn + ' wins!')
                break
            else:
                if(isBoardFull(Board)):
                    print('The game is a tie!')
                    return
        if turn=='player':
            turn='computer'
        else:
            turn='player'
    printBoard(Board)
play()
    

    
