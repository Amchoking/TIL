class Solution:
    def longestPalindrome(self, s: str) -> str:
        strsize=len(s)
        maxlen=1
        start=0
        end=-0
        matrix = [[False for i in range(strsize)] for j in range(strsize)]
        
        for i in range(strsize):
            matrix[i][i]=True
                
        for i in range(strsize-1):
            if(s[i] == s[i+1]):
                matrix[i][i+1]=True
                if(maxlen<2):
                    start=i
                    end=i+1
                    maxlen=2
        
        for i in range(2,strsize):
            for j in range(strsize-i):
                if(matrix[j+1][j+i-1] and s[j] == s[j+i]):
                    matrix[j][j+i] = True
                    if(maxlen<i+1):
                        maxlen=i+1
                        start=j
                        end=j+i
        
        answer =""
        for i in range(start,end+1):
            answer=answer+s[i]
        
        return answer
