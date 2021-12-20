class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lennum=len(nums)
        answer =0
        for i in range(lennum):
            answer=answer^nums[i]
        return answer
