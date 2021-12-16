class Solution:
    def jump(self, nums: List[int]) -> int:
        maxlength=0
        curlength=0
        jump=0
        if(len(nums)==1): return 0
        for i in range(len(nums)):
            maxlength = max(maxlength,i+nums[i])
            if(i==curlength):
                curlength=maxlength
                jump=jump+1
            if(len(nums)-1 <= curlength):
                break
        return jump
        
