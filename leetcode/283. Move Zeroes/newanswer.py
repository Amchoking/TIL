class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        for i in range(len(nums)):
            if(nums[i-count]==0):
                nums.pop(i-count)
                nums.append(0)
                count=count+1
