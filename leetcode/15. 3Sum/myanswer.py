class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsdict={}
        checkdict={}
        answer=[]
        for i in range(len(nums)):
            if(nums[i] in numsdict):
                numsdict[nums[i]]=numsdict[nums[i]]+1
            else:
                numsdict[nums[i]]=1
        
        keylist=list(numsdict.keys())
        for i in range(0,len(keylist)):
            for j in range(i+1,len(keylist)):
                lastnum= -(keylist[i]+keylist[j])
                if(lastnum in numsdict):
                    checklist=[keylist[i],keylist[j],lastnum]
                    checklist.sort()
                    checkstring=str(checklist[0])+" "+str(checklist[1])+" "+str(checklist[2])
                    if(checkstring in checkdict):
                        continue
                    if(lastnum == keylist[i]):
                        if(numsdict[keylist[i]]>=2):
                            answer.append([keylist[i],keylist[j],lastnum])
                            checkdict[checkstring]=True
                    elif(lastnum == keylist[j]):
                        if(numsdict[keylist[j]]>=2):
                            answer.append([keylist[i],keylist[j],lastnum])
                            checkdict[checkstring]=True
                    else:
                        answer.append([keylist[i],keylist[j],lastnum])
                        checkdict[checkstring]=True
        if(0 in numsdict):
            if(numsdict[0]>=3):
                answer.append([0,0,0])
        return answer
