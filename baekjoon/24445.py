import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(r):
    global visited,nodes
    count=1
    visited[r] = count
    count+=1
    nextgo=[r]
    while(len(nextgo)!=0):
        k=nextgo.pop(0)
        listnode = nodes[k]
        listnode.sort(reverse=True)
        for j in range (len(listnode)):
            if(visited[listnode[j]]==0):
                visited[listnode[j]]=count
                count+=1
                nextgo.append(listnode[j])

n,m,r = map(int,input().split())
visited =[0 for i in range(n+1)]
nodes = { k: [] for k in range(n+1)}
for i in range (m):
    a,b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

bfs(r)
for i in range(1,n+1):
    print(visited[i])