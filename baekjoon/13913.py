import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = [-1 for i in range(200001)]
check = [-1 for i in range(200001)]

dp[n] = 0

queue = []
now = n
while(now!=k):
    if(now+1 <= 200000 and dp[now+1] == -1):
        dp[now+1] = dp[now]+1
        check[now+1] = now
        if(now+1 == k):
            break
        queue.append(now+1)
    if(now-1 >= 0 and dp[now-1] == -1):
        dp[now-1] = dp[now]+1
        check[now-1] = now
        if(now-1 == k):
            break
        queue.append(now-1)
    if(now*2 <= 200000 and dp[now*2] == -1):
        dp[now*2] = dp[now]+1
        check[now*2] = now
        if(now*2 == k):
            break
        queue.append(now*2)
    now = queue.pop(0)

print(dp[k])
now = k
answer = []
while(now!=n):
    answer.append(now)
    now = check[now]
answer.append(n)
answer.reverse()
print(*answer)