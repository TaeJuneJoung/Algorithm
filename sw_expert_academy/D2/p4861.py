import sys
sys.stdin = open('../input/p4861.txt', 'r')

def check(N,M,arr):
    for n in range(N):
        for i in range(N-M+1):
            res = ""
            for j in range(M):
                if arr[n][j+i] == arr[n][M-1+i-j]:
                    res += arr[n][j+i]
                    if len(res) == M:
                        return res

    for n in range(N):
        for i in range(N-M+1):
            res = ""
            for j in range(M):
                if arr[i+j][n] == arr[M-1+i-j][n]:
                    res += arr[i+j][n]
                    if len(res) == M:
                        return res

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [0 for i in range(N)]
    for n in range(N):
        arr[n] = input()
    res = check(N,M,arr)

    print(f"#{t} {res}")