class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check={}
        for i in range(len(nums)):
            if(nums[i] in check):
                return True
            else:
                check[nums[i]]=True
        return False
