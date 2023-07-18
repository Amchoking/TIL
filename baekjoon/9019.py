import sys
from collections import deque
input = sys.stdin.readline
check = [[] for i in range(10000)]
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    array=[-1 for i in range (10000)]
    array[a] = 0
    queue = deque([a])
    now = a
    while(now != b):
        now = queue.popleft()
        if(now*2>=10000 and array[now*2-10000] == -1):
            array[now*2-10000] = array[now]+1
            check[now*2-10000] = [now,'D']
            queue.append(now*2-10000)
            if(now*2-10000 == b):
                break
        elif(now*2<10000 and array[now*2] == -1):
            array[now*2] = array[now]+1
            check[now*2] = [now,'D']
            queue.append(now*2)
            if(now*2 ==b):
                break
        #D
        
        if(now ==0 and array[9999] == -1):
            array[9999] = array[0]+1
            check[9999] = [now,'S']
            queue.append(9999)
            if(b==9999):
                break
        elif(array[now-1] == -1):
            array[now-1] = array[now]+1
            check[now-1] = [now,'S']
            queue.append(now-1)
            if(b==now-1):
                break
        #S
        
        nextl = (now%1000)*10+(now//1000)
        if(array[nextl] == -1):
            array[nextl] = array[now]+1
            check[nextl] = [now,'L']
            queue.append(nextl)
            if(nextl==b):
                break
        #L
        
        nextr = (now%10)*1000 + (now//10)
        if(array[nextr]==-1):
            array[nextr] = array[now]+1
            check[nextr] = [now,'R']
            queue.append(nextr)
            if(nextr == b):
                break
        #R
    answer = []
    current = b
    while(current != a):
        answer.append(check[current][1])
        current = check[current][0]
    answer.reverse()
    print(''.join(answer))