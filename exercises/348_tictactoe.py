
class TicTacToe:
    # On space On
    def __init__(self, n: int):
        self.n = n
        self.diag=0
        self.adiag=0
        self.rows = [0]*n
        self.cols = [0]*n
        
    #O1
    def move(self, row: int, col: int, player: int) -> int:
        pt = 1 if player == 1 else -1
        self.rows[row]+=pt
        self.cols[col]+=pt
        if row==col:
            self.diag+=pt
        if row+col==self.n-1:
            self.adiag+=pt
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag)==self.n or abs(self.adiag)==self.n:
            return player
        return 0
    

#variant: given board, single move check if won
def isWin(board,player,row,col):
    board[row][col] = player
    rows=cols=diag=adiag=0
    n=len(board)
    for i in range(n):
        if board[row][i]==player:
            rows+=1
        if board[i][col]==player:
            cols+=1
        if board[i][i]==player:
            diag+=1
        if board[i][n-1-i]==player:
            adiag+=1
        return rows==n or cols==n or diag==n or adiag==n