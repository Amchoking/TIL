class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memory={}
        maxtime=0
        maxnum=0
        for i in range(len(nums)):
            if(nums[i] in memory):
                memory[nums[i]]=memory[nums[i]]+1
            else:
                memory[nums[i]]=1
            if(maxtime<memory[nums[i]]):
                maxtime=memory[nums[i]]
                maxnum=nums[i]
        return maxnum
