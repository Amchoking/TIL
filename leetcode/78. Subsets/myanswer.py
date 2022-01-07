class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        empty=[[]]
        for i in range(len(nums)):
            for j in range(len(empty)):
                new_subset=empty[j][:]
                new_subset.append(nums[i])
                empty.append(new_subset)
        return empty
