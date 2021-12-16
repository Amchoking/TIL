class Solution:
    def jump(self, nums: List[int]) -> int:
        lennum=len(nums)
        queuearray=[]
        checkmin=[9999 for i in range(lennum)]
        checkmin[0]=0
        queuearray.append(0)
        queuepointer=0
        while(queuepointer<len(queuearray)):
            now = queuearray[queuepointer]
            nowcheck=checkmin[now]
            if(now+nums[now]>lennum-1):
                maxnum=lennum-1
            else:
                maxnum=now+nums[now]
            for i in range(now+1,maxnum+1):
                if(checkmin[i]>nowcheck+1):
                    queuearray.append(i)
                    checkmin[i]=nowcheck+1
            queuepointer=queuepointer+1
        return checkmin[lennum-1]
        
