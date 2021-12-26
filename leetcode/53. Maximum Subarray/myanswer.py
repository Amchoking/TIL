class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nowsum=0
        maxval=-1000000
        for i in range(len(nums)):
            nowsum=nowsum+nums[i]
            maxval=max(maxval, nowsum)
            if(nowsum<0):
                nowsum=0
        return maxval
