class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        answer=[""]
        new_answer=[]
        if(digits == ""):
            return new_answer
        for i in digits:
            new_answer=[]
            for j in answer:
                for k in alpha[i]:
                    new_answer.append(j+k)
            answer=new_answer[:]
        return answer
