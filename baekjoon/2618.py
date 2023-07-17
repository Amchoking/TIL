import sys
input = sys.stdin.readline

n = int(input())
w = int(input())
array = [[-1 for j in range(w+1)] for i in range(w+1)]
check = [[[-1,-1] for j in range(w+1)] for i in range(w+1)]
todo = [[0,0]]
for i in range(w):
    a,b = map(int,input().split())
    todo.append([a,b])

for i in range (w+1):
    for j in range(w+1):
        if(i==0 and j==0):
            array[0][0] = 0
        elif(i==0 and j==1):
            array[i][j] = array[i][j-1] + abs(todo[j][0]-n) + abs(todo[j][1]-n)
            check[i][j] = [i,j-1]
        elif(i==1 and j==0):
            array[i][j] = array[i-1][j] + abs(todo[i][0]-1) + abs(todo[i][1]-1)
            check[i][j] = [i-1,j]
        elif(i==0):
            array[i][j] = array[i][j-1] + abs(todo[j][0]-todo[j-1][0]) + abs(todo[j][1]-todo[j-1][1])
            check[i][j] = [i,j-1]
        elif(j==0):
            array[i][j] = array[i-1][j] + abs(todo[i][0]-todo[i-1][0]) + abs(todo[i][1]-todo[i-1][1])
            check[i][j] = [i-1,j]
        elif(abs(i-j) != 1):
            if(i<j):
                array[i][j] = array[i][j-1] + abs(todo[j][0]-todo[j-1][0]) + abs(todo[j][1]-todo[j-1][1])
                check[i][j] = [i,j-1]
            elif(i==j):
                pass
            else:
                array[i][j] = array[i-1][j] + abs(todo[i][0]-todo[i-1][0]) + abs(todo[i][1]-todo[i-1][1])
                check[i][j] = [i-1,j]
        else:
            if(i<j):
                array[i][j] = array[i][0] + abs(todo[j][0]-n) + abs(todo[j][1]-n)
                check[i][j] = [i,0]
                for k in range(1,j-1):
                    klen = array[i][k] + abs(todo[j][0]-todo[k][0]) + abs(todo[j][1]-todo[k][1])
                    if(array[i][j] > klen):
                        array[i][j] = klen
                        check[i][j] = [i,k]
            else:
                array[i][j] = array[0][j] + abs(todo[i][0]-1) + abs(todo[i][1]-1)
                check[i][j] = [0,j]
                for k in range(1,i-1):
                    klen = array[k][j] + abs(todo[i][0]-todo[k][0]) + abs(todo[i][1]-todo[k][1])
                    if(array[i][j] > klen):
                        array[i][j] = klen
                        check[i][j] = [k,j]

minvalue = 1000000
a = 0
b = 0
for i in range (w):
    if(array[i][w]<minvalue):
        minvalue = array[i][w]
        a = i
        b = w
    if(array[w][i]<minvalue):
        minvalue = array[w][i]
        a = w
        b = i

answer = []
while(a!=0 or b!=0):
    if (a<b):
        answer.append(2)
    else:
        answer.append(1)
    a,b = check[a][b]
answer.reverse()
print(minvalue)
for i in range(len(answer)):
    print(answer[i])