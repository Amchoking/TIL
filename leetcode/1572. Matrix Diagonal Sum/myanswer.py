class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sumn=0
        for i in range(n):
            sumn=sumn+mat[i][i]+mat[n-i-1][i]
        if(n%2==1):
            sumn=sumn-mat[n//2][n//2]
        return sumn
