class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numdict={}
        for i in range(len(nums)):
            if(nums[i] in numdict):
                return nums[i]
            else:
                numdict[nums[i]]=True
