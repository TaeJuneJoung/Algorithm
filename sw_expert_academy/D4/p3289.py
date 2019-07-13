import sys
sys.stdin = open('../input/p3289.txt', 'r')


def make_set(x):
    p[x] = x
    rank[x] = 0

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x,y):
    px = find_set(x)
    py = find_set(y)

    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    
    p = [0]*(N+1)
    rank = [0]*(N+1)

    res = "#"+str(t)+" "

    for i in range(1,N+1):
        make_set(i)

    for i in range(1,M+1):
        oper, a, b = map(int, input().split())
        if oper == 0:
            union(a,b)
        else:
            if find_set(a) == find_set(b):
                res += "1"
            else:
                res += "0"
    print(res)