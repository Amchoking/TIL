class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x,y = len(matrix[0]),len(matrix)
        nowx,nowy=0,0
        up=True
        answer=[]
        while(x>0 and y>0):
            if(up):
                for i in range(x):
                    answer.append(matrix[nowy][nowx])
                    nowx=nowx+1
                nowx=nowx-1
                for i in range(y-1):
                    nowy=nowy+1
                    answer.append(matrix[nowy][nowx])
                nowx=nowx-1
            else:
                for i in range(x):
                    answer.append(matrix[nowy][nowx])
                    nowx=nowx-1
                nowx=nowx+1
                for i in range(y-1):
                    nowy=nowy-1
                    answer.append(matrix[nowy][nowx])
                nowx=nowx+1
            up=not up
            x=x-1
            y=y-1
        return answer
