from math import sqrt

def isrowsafe(board,row,i,N):
    for j in range(N):
        if board[row][j]==i:
            return False
    return True
    
def iscolsafe(board,col,i,N):
    for j in range(N):
        if board[j][col]==i:
            return False
    return True
    
def isboxsafe(board,row,col,i,N):
    row_s=row-row%int(sqrt(N))
    col_s=col-col%int(sqrt(N))
    for k in range(row_s,row_s+int(sqrt(N))):
        for j in range(col_s,col_s+int(sqrt(N))):
            if board[k][j]==i:
                return False
    return True
    
def canplace(board,row,col,i,N):
    if isrowsafe(board,row,i,N) and iscolsafe(board,col,i,N) and isboxsafe(board,row,col,i,N):
        return True
    return False

def suduko_solver(board, N):
    row=-1
    col=-1
    isempty=False
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                row=i
                col=j
                isempty=True
            if(isempty):
                break
        if(isempty):
            break
    
    if not isempty:
        return True
    
    for i in range(1,N+1):
        if canplace(board,row,col,i,N):
            board[row][col]=i
            if suduko_solver(board, N):
                return True
        board[row][col]=0
        
    return False

    board=[]
    M=list(int(i) for i in input().split())
    for i in range(0,len(M),9):
        board.append(M[i:i+9])
    N=len(board)
    suduko_solver(board, N)
    for i in board:
        print(' '.join(map(str,i)),end=' ')
    print()