import sys
sys.stdin = open('../input/p2001.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    max_val = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_val = 0
            for mi in range(M):
                for mj in range(M):
                    sum_val += arr[i+mi][j+mj]
            max_val = sum_val if sum_val > max_val else max_val

    print(f"#{t} {max_val}")