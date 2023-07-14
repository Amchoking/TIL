import sys
input = sys.stdin.readline

n = int(input())
stackn = []
count = 0
for i in range(n):
    k = int(input())
    lenn = len(stackn)
    check = 0
    save = 0
    value = 0
    for j in range(lenn):
        if(stackn[j][0]<=k):
            count+=stackn[j][1]
        else:
            count+=1
            break
        if(stackn[j][0]==k):
            save = j
            check = 1
            value = k
        elif(stackn[j][0]<k):
            save = j+1
            check = 2
            value = k
    if(check == 0):
        stackn.insert(0,[k,1])
    elif(check == 1):
        del stackn[0:save]
        stackn[0][1] += 1
    elif(check == 2):
        del stackn[0:save]
        stackn.insert(0,[k,1])

print(count)