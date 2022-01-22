class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for n in nums:
            cur = abs(n)
            if nums[cur-1] > 0:
                nums[cur-1] *= -1
        
        resp = []
        for i, num in enumerate(nums):
            if num > 0:
                resp.append(i+1)
                
        return resp
