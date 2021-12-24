class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversedigits = digits[::-1]
        val =0
        up=1
        answer=[]
        for i in range(len(digits)):
            val = (reversedigits[i]+up)%10
            up=(reversedigits[i]+up)//10
            answer.append(val)
        if(up==1):
            answer.append(1)
        return answer[::-1]
