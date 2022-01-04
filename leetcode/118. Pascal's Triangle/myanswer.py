class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer=[]
        for i in range(numRows):
            new_row=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    new_row.append(1)
                else:
                    new_row.append(answer[i-1][j-1]+answer[i-1][j])
            answer.append(new_row)
        return answer
