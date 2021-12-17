class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxlength=0
        curlength=0
        jump=0
        if(len(nums)==1): return True
        for i in range(len(nums)):
            maxlength = max(maxlength,i+nums[i])
            if(i==curlength):
                curlength=maxlength
                jump=jump+1
            if(len(nums)-1 <= curlength):
                return True
        return False
