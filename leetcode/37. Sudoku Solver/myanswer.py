class Solution:
    def __init__(self):
        self.gugu = [[0 for col in range(9)] for row in range(9)]
        self.canx = [[False for col in range(10)] for row in range(10)] 
        self.cany = [[False for col in range(10)] for row in range(10)]
        self.cansq=[[[False for i in range(10)] for j in range (10)] for k in range(10)]
        self.solved = False
        
    def solve(self,cnt):
        if(cnt==81):
            self.solved=True
            return
        x=cnt//9
        y=cnt%9
        if(self.gugu[x][y]):
            self.solve(cnt+1)
        else:
            for k in range (1,10):
                if((not self.canx[x][k]) and (not self.cany[y][k]) and (not self.cansq[x//3][y//3][k])):
                    self.canx[x][k]=True
                    self.cany[y][k]=True
                    self.cansq[x//3][y//3][k]=True
                    self.gugu[x][y]=k
                    self.solve(cnt+1)

                    if(self.solved):
                        return

                    self.canx[x][k]=False
                    self.cany[y][k]=False
                    self.cansq[x//3][y//3][k]=False
                    self.gugu[x][y]=0
                    
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='.'):
                    self.gugu[i][j]==0
                else:
                    self.gugu[i][j]=int(board[i][j])
                    if(self.canx[i][self.gugu[i][j]] or self.cany[j][self.gugu[i][j]] or self.cansq[i//3][j//3][self.gugu[i][j]]):
                        return False
                    self.canx[i][self.gugu[i][j]]=True
                    self.cany[j][self.gugu[i][j]]=True
                    self.cansq[i//3][j//3][self.gugu[i][j]]=True
        self.solve(0)
        for i in range(9):
            for j in range(9):
                board[i][j]=str(self.gugu[i][j])
        
