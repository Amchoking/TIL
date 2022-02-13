class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(num1=="0" or num2=="0"):
            return "0"
        n1=num1[::-1]
        n2=num2[::-1]
        answer=[]
        for i in range(len(n1)):
            for j in range(len(n2)):
                addnum=int(n1[i])*int(n2[j])
                if(len(answer)==i+j):
                    answer.append(addnum)
                else:
                    answer[i+j]=answer[i+j]+addnum
        for i in range(len(answer)):
            if(i==len(answer)-1):
                if(answer[i]>=10):
                    answer.append(answer[i]//10)
            else:
                answer[i+1]=answer[i+1]+answer[i]//10
            answer[i]=answer[i]%10
        return "".join([str(a) for a in answer[::-1]])
