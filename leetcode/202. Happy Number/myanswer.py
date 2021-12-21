class Solution:
    def isHappy(self, n: int) -> bool:
        nums={}
        if(n==1): return True
        while(n!=1):
            nums[n]=True
            check=0
            while(n>0):
                check=check+((n%10)*(n%10))
                n=n//10
            if(check in nums):
                return False
            elif(check==1):
                return True
            else:
                n=check
