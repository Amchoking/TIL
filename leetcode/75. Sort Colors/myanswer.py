class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count=[0,0,0]
        for i in nums:
            if(i==0):
                count[0]=count[0]+1
            elif(i==1):
                count[1]=count[1]+1
            else:
                count[2]=count[2]+1
        now=0
        for i in range(3):
            for J in range(count[i]):
                nums[now]=i
                now=now+1
