import sys
from collections import Counter
input = sys.stdin.readline

a = int(input())
lista = list(map(int,input().split()))
dicta = Counter(lista)
stacka=[]
result = [-1]*a

for i in range(a):
    while(stacka and dicta[lista[stacka[-1]]]<dicta[lista[i]]):
        result[stacka.pop()] = lista[i]
    stacka.append(i)
    
print(*result)