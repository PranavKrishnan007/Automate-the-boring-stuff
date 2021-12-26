board = {'top-L':' ', 'top-M':' ', 'top-R':' ',
         'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
         'low-L':' ', 'low-M':' ', 'low-R':' '}
         
def boardprint(dict):
    print(board['top-L'] + '|' + board['top-M'] + '|'+ board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X' 
for i in range(9):
    boardprint(board)
    print(turn + '. move?')
    move = input()
    board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
