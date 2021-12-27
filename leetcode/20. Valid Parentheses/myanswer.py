class Solution:
    def isValid(self, s: str) -> bool:
        lens=len(s)
        array=[]
        pair = {')':'(',']':'[','}':'{'}
        for i in range(lens):
            if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
                array.append(s[i])
            else:
                if(len(array)==0):
                    return False
                elif(array[len(array)-1]==pair[s[i]]):
                    array.pop()
                else:
                    return False
        if(len(array)==0):
            return True
        return False
