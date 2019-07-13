import sys
input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    M = [0 for i in range(N)]
    for i in range(N):
        M[i] = list(map(int,input().split()))
    M.sort()
    
    limit = M[0][1]
    cnt = 1

    for i in range(1,N):
        if limit > M[i][1]:
            cnt += 1
            limit = M[i][1]
    print(cnt)