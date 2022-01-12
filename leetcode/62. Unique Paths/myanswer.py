class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer=1
        for i in range(m,m+n-1):
            answer=answer*i
        for j in range(1,n):
            answer=answer/j
        return int(answer)
