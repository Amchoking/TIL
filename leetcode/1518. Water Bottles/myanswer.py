class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer=numBottles
        empty=numBottles
        while(empty>=numExchange):
            answer=answer+(empty//numExchange)
            empty=(empty%numExchange)+(empty//numExchange)
        return answer
