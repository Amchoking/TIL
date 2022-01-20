class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeropoint=0
        changepoint=zeropoint+1
        while(zeropoint<len(nums)-1):
            if(nums[zeropoint]==0):
                changepoint=zeropoint+1
                while(nums[changepoint]==0):
                    changepoint=changepoint+1
                    if(changepoint>=len(nums)):
                        return
                nums[zeropoint]=nums[changepoint]
                nums[changepoint]=0
            else:
                zeropoint=zeropoint+1
