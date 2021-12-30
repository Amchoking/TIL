class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<=0):
            return False
        elif(n&(-n)==n):
            if(int(n**0.5)==n**0.5):
                return True
        return False
