class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        answer=[[]]
        for i in range(n):
            for j in range(len(answer)):
                for k in range(i+1):
                    new=answer[0][:]
                    new.insert(k,nums[i])
                    answer.append(new)
                answer.pop(0)
        return answer
