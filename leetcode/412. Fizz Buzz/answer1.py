class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(n):
            answer.append(str(i+1))
        for i in range(n//3):
            answer[i*3+2]="Fizz"
        for i in range(n//5):
            answer[i*5+4]="Buzz"
        for i in range(n//15):
            answer[i*15+14]="FizzBuzz"
        return answer
