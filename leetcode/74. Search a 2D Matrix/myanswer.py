class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(matrix[0][0]>target):
            return False
        check=0
        for i in range(len(matrix)):
            if(matrix[i][0]<=target):
                check=i
            else:
                break
        for i in range(len(matrix[0])):
            if(matrix[check][i]==target):
                return True
        return False
