class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        lens = len(s)
        nownum=0
        lastnum=0
        for i in range(lens):
            if(i==0):
                nownum=nownum+roman[s[i]]
                lastnum=roman[s[i]]
            else:
                thisnum=roman[s[i]]
                if(lastnum<thisnum):
                    nownum=nownum+thisnum-(2*lastnum)
                else:
                    nownum=nownum+thisnum
                lastnum=roman[s[i]]
            
        return nownum
