class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last=0
        longest=0
        indexs={}
        for i in range(len(s)):
            if (s[i] in indexs):
                if(indexs[s[i]]>=last):
                    if(i-last > longest):
                        longest = i-last
                    last=indexs[s[i]]+1
                indexs[s[i]]=i
            else:
                indexs[s[i]]=i
        if(len(s)-last > longest):
            longest = len(s)-last
        return longest
