class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        savedata=[]
        days=len(temperatures)
        answer=[0 for i in range(days)]
        for i in range(days):
            while(savedata and temperatures[i]>savedata[0][0]):
                a,b = savedata.pop(0)
                answer[b]=i-b
            savedata.insert(0,[temperatures[i],i])
        return answer
