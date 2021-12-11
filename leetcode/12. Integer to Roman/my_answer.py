class Solution:
    def intToRoman(self, num: int) -> str:
        array=[1000,500,100,50,10,5]
        check=[900,400,90,40,9,4]
        roman=['M','D','C','L','X','V','I']
        answer=""
        for i in range(len(array)):
            n=num//array[i]
            m=num%array[i]
            for j in range(n):
                answer= answer+roman[i]
            num=m
            if(num >= check[i]):
                if(i%2==0):
                    answer=answer+roman[i+2]+roman[i]
                else:
                    answer=answer+roman[i+1]+roman[i]
                num=num-check[i]
        for i in range(num):
            answer=answer+roman[6];
        return answer
