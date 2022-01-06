class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudokuset=set([])
        
        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    if(board[i][j] in sudokuset):
                        return False
                    sudokuset.add(board[i][j])
            sudokuset.clear()
        
        for j in range(9):
            for i in range(9):
                if(board[i][j]!='.'):
                    if(board[i][j] in sudokuset):
                        return False
                    sudokuset.add(board[i][j])
            sudokuset.clear()
        
        for i1 in range(3):
            for j1 in range(3):
                for i2 in range(3):
                    for j2 in range(3):
                        if(board[i1*3+i2][j1*3+j2]!='.'):
                            if(board[i1*3+i2][j1*3+j2] in sudokuset):
                                return False
                            sudokuset.add(board[i1*3+i2][j1*3+j2])
                sudokuset.clear()
        
        return True
