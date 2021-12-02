class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = 202
        error = False
        checkingarray = strs[0]
        for i in strs:
            if(len(i)<minlen):
                minlen = len(i)
        
        for i in range(len(strs)):
            for j in range(minlen):
                if (i!=0 and checkingarray[j] != strs[i][j]):
                    minlen=j
                    break
        
        return checkingarray[0:minlen]
