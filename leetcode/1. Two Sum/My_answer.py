class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums:
            if(target-n in nums[nums.index(n)+1: ]):
                return [nums.index(n), nums.index(target-n,nums.index(n)+1)]
