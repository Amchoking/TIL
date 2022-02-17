class Solution:
    def __init__(self):
        self.n=0
        self.nums=[]
        self.dict1={}
        self.dict2={}
    def add1(self,location: int, nowsum:int, addversion: int):
        if(addversion==1):
            if((self.n)//2==location):
                if(nowsum in self.dict1):
                    self.dict1[nowsum]=self.dict1[nowsum]+1
                else:
                    self.dict1[nowsum]=1
                return
            self.add1(location+1,nowsum+self.nums[location],1)
            self.add1(location+1,nowsum-self.nums[location],1)
        else:
            if((self.n)==location):
                if(nowsum in self.dict2):
                    self.dict2[nowsum]=self.dict2[nowsum]+1
                else:
                    self.dict2[nowsum]=1
                return
            self.add1(location+1,nowsum+self.nums[location],2)
            self.add1(location+1,nowsum-self.nums[location],2)
            
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.n=len(nums)
        self.nums=nums
        self.add1(0,0,1)
        self.add1(self.n//2,0,2)
        answer=0
        for i in self.dict1.keys():
            if(target-i in self.dict2):
                answer=answer+(self.dict1[i]*self.dict2[target-i])
        return answer
