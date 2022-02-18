class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        checkarray=[]
        answer=[]
        count=0
        nownum=0
        for i in range(len(nums)):
            if(i==0):
                nownum=nums[i]
                count=1
            else:
                if(nownum==nums[i]):
                    count=count+1
                else:
                    checkarray.append([count,nownum])
                    nownum=nums[i]
                    count=1
        checkarray.append([count,nownum])
        checkarray.sort()
        for i in range(k):
            answer.append(checkarray[len(checkarray)-1-i][1])
        return answer
