theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
board_keys = []

for key in theBoard:
    board_keys.append(key)

blya = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def checkSpan(value):
    if value in blya:
        return True
    else:
        return False
def checkOX(value):
    if value == 'X' or value == 'O':
        return True
    else:
        return False
        
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])    
   
def vvodDlyaDebilov():
    while True:
        print('Enter num: ')
        move = input()
        ind = checkSpan(move)
        if ind == True:
            ind = checkOX(theBoard[move])
            if ind == False:
                
                return move
    
def pointer():
    turn = 'X'
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn)
        move = vvodDlyaDebilov()
        theBoard[move] = turn
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
            printBoard(theBoard)                            
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
            printBoard(theBoard)              
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
            printBoard(theBoard)               
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)              
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
            printBoard(theBoard)               
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
            printBoard(theBoard)               
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
            printBoard(theBoard)               
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
            printBoard(theBoard)               
            break 
               
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 

pointer()
print('Game over.')
