class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        negative = 1
        num=x
        if(x<0):
            negative=-1
            num=num*(-1)
        numstr = str(num)
        reversenum = numstr[::-1]
        skip=0
        
        for i in range(len(reversenum)):
            if(reversenum[i] == '0'):
                skip=i+1
            else:
                break
        
        answer = int(reversenum[skip:len(reversenum)])*negative
        if(answer>2147483647 or answer<-2147483648):
            return 0
        return answer
