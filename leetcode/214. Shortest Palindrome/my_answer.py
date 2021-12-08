class Solution:
    def shortestPalindrome(self, s: str) -> str:
        lens = len(s)
        maxlen=0
        start=-1
        end=-1
        answer=""
        for i in range (lens+1):
            if(s[0:i] == s[i-1::-1] and maxlen < i):
                maxlen = i
                start=0
                end = i
        if (start==0):
            for i in range(end,lens):
                answer=s[i]+answer
            answer=answer+s
        return answer
