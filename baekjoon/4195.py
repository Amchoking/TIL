import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(name):
    if (name != names[name][0]):
        return find_parent(names[name][0])
    return names[name][0]

t= int(input().rstrip())
for i in range(t):
    n = int(input().rstrip())
    names={}
    for j in range(n):
        name1, name2 = input().rstrip().split()
        if(name1 in names):
            p1 = find_parent(name1)
            names[name1][0]=p1
        else:
            names[name1]= [name1,1]
            p1 = name1
            
        if(name2 in names):
            p2 = find_parent(name2)
            names[name2][0] = p2
        else:
            names[name2] = [name2,1]
            p2 = name2
            
        if(p1 != p2):
            if(p1 < p2):
                names[p2][0] = names[p1][0]
                names[p2][1] += names[p1][1]
                names[p1][1] = names[p2][1]
            else:
                names[p1][0] = names[p2][0]
                names[p2][1] += names[p1][1]
                names[p1][1] = names[p2][1]
        print(names[p2][1])