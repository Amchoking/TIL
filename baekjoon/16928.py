import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(r):
    global visited,nodes
    visited[r] = 0
    nextgo=[r]
    while(len(nextgo)!=0):
        k=nextgo.pop(0)
        if (k==100):
            return visited[100]
        for i in range(1,7):
            if(k+i<=100):
                if(visited[k+i]==0):
                    visited[k+i]=visited[k]+1
                    if((k+i) in nodes):
                        if(visited[nodes[k+i]]==0):
                            nextgo.append(nodes[k+i])
                            visited[nodes[k+i]]=visited[k]+1
                    else:
                        nextgo.append(k+i)

n,m = map(int,input().split())
visited =[0 for i in range(101)]
nodes = {}
for i in range (n+m):
    a,b = map(int,input().split())
    nodes[a]=b

print(bfs(1))
