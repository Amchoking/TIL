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
        
        answerstr = reversenum[skip:len(reversenum)]
        if(len(answerstr)>9) and (answerstr>"2147483648" or (answerstr == "2147483648" and negative == 1)):
            return 0
        answer = int(answerstr)*negative
        return answer
