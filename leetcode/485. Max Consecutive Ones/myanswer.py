class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcon=0
        countnow=0
        for i in nums:
            if(i==0):
                maxcon=max(maxcon,countnow)
                countnow=0
            else:
                countnow=countnow+1
        maxcon=max(maxcon,countnow)
        return maxcon
