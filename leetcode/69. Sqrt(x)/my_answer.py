class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return 0
        movesize = (x+1)//2
        now=movesize
        movesize=(movesize+1)//2
        while(movesize>0):
            if(now*now<=x and (now+1)*(now+1)>x):
                return now
            if(now*now>x):
                now=now-movesize
                movesize=(movesize+1)//2
            elif((now+1)*(now+1)<=x):
                now=now+movesize
                movesize=(movesize+1)//2
