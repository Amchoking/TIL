class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue=prices[0]
        maxvalue=0
        answer=0
        for i in range(1,len(prices)):
            if(minvalue>prices[i]):
                minvalue=prices[i]
                maxvalue=0
            elif(maxvalue<prices[i]):
                maxvalue=prices[i]
                answer=max(maxvalue-minvalue,answer)
        return answer
