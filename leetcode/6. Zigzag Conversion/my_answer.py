class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        else:
            new_s=""
            rule = numRows*2-2
            for i in range(numRows):
                if(i == 0 or i == numRows-1):
                    now=i
                    while(now<len(s)):
                        new_s=new_s+s[now]
                        now=now+rule
                else:
                    now=i
                    while(now<len(s)):
                        new_s=new_s+s[now]
                        now=now+rule-(i*2)
                        if(now>=len(s)):
                            break
                        new_s=new_s+s[now]
                        now=now+(i*2)
            return new_s
