class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return 1
        else:
            fibo=[1,1]
            for i in range(n-1):
                fibo.append(fibo[i]+fibo[i+1])
            return fibo[n]
