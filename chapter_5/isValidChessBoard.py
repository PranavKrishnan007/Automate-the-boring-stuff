board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(chess):
    #to check if the given board is valid or not, ref - 16 pieces, 8 pawns, 1 king, 1 queen, 2 bishops, 2 rooks and 2 knights
    bpieces = ['bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']
    wpieces = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking']
    pieces = bpieces + wpieces
    ans = True
    bpcount,wpcount = 0,0
    bpiecec,wpiecec = 0,0 
    pos_v = list('abcdefgh')
    pos_h = list('12345678')
    pos = []
    for x in range(8):
        for i in range(8):
            pos.append(pos_h[x] + pos_v[i]) 
    
    for x in chess.keys():
        if x not in pos:
            ans = False

    for x in chess.values():
        if x not in pieces:
            ans = False

    #pawncount 
    for x in chess.values():
        if x == 'bpawn' :
            bpcount += 1
        elif x == 'wpawn':
            bpcount += 1
    if bpcount > 8 or wpcount > 8:
        ans = False
        
    #piececount 
    for x in chess.values():
        if x in bpieces:
            bpiecec += 1
        elif x in wpieces:
            wpiecec += 1
    if bpiecec > 8 or wpiecec > 8:
        ans = False
        
    return(ans)

print(isValidChessBoard(board))
