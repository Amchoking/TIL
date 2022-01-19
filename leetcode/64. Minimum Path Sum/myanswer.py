class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0 for i in range(len(grid[0]))]for j in range(len(grid))]
        dp[0][0]=grid[0][0]
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if(i==0 and j==0):
                    continue
                elif(i==0):
                    dp[j][0]=dp[j-1][0]+grid[j][0]
                elif(j==0):
                    dp[0][i]=dp[0][i-1]+grid[0][i]
                else:
                    dp[j][i]=min(dp[j-1][i],dp[j][i-1])+grid[j][i]
        return dp[len(grid)-1][len(grid[0])-1]
