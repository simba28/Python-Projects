import random 
from os import system, name

# to clear the screen
def clear():
    # for windows
    if name=='nt':
        _ = system('cls')

    # for linux and mac ( here os.name is 'posix')
    else:
        _ = system('clear')


def AssignSign(move, val):
    if move<=3:
        if move==1:
            board[0][0]=val
        elif move==2:
            board[0][1]=val
        else:
            board[0][2]=val
    elif move<=6:
        if move==4:
            board[1][0]=val
        elif move==5:
            board[1][1]=val
        else:
            board[1][2]=val
    else:
        if move==7:
            board[2][0]=val
        elif move==8:
            board[2][1]=val
        else:
            board[2][2]=val
    return board


def DisplayBoard(board):
    
    clear()

    print('TIC TAC TOE')

    for x in board:
        print('+-----------------------+')
        print('|       |       |       |')
        print(f'|   {x[0]}   |   {x[1]}   |   {x[2]}   |')
        print('|       |       |       |')
    print('+-----------------------+')


def EnterMove(board):
    lst = MakeListOfFreeFields(board)
    global playOn
    if len(lst)==0:
        print('Game Tie!!')
        playOn = False

    else:
        cond = True

        while(cond):
            move = int(input('Enter your move : '))
            if( move>0 and move<10 and (move in lst)):
                cond = False
            else:
                print('that place already filled!')
        
        board = AssignSign(move,'O')
        VictoryFor(board,'O')

    return board
    

def MakeListOfFreeFields(board):
    free_lst = []
    global playOn
    for x in board:
        free_lst.extend(x)
    free_lst = list(filter(lambda n: type(n)==int, free_lst))
    
    return free_lst


def VictoryFor(board, sign):
    global playOn
    for x in range(3):
        if board[x][0]==board[x][1]==board[x][2]:
            playOn = False
            break
        elif board[0][x]==board[1][x]==board[2][x]:
            playOn = False
            break

    if board[0][0]==board[1][1]==board[2][2]:
        playOn = False
    elif board[0][2]==board[1][1]==board[2][0]:
        playOn = False
    
    DisplayBoard(board)
    user = 'You' if sign=='O' else 'Computer'
    if playOn == False:
        print(user,'won!')


def DrawMove(board):
    free_lst = MakeListOfFreeFields(board)
    if len(free_lst)>0:
        move = random.choice(free_lst)
        board = AssignSign(move, 'X')
        VictoryFor(board,'X')

    return board


if __name__=='__main__':
    # clear()
    board = [[1,2,3],[4,'X',6],[7,8,9]]
    playOn = True
    DisplayBoard(board)
    while(playOn):
        board = EnterMove(board)
        if playOn == False:
            break
        board = DrawMove(board)
        if playOn == False:
            break
