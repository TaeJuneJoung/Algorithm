#제출시 제출결과에 맞게 수정필요

import sys
sys.stdin = open("input/test2.txt", "r")

T = int(input())
for t in range(1,T+1):
    # 백준
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1,1<<N):
        result = 0
        for j in range(N):
            if i & 1<<j != 0:
                result += arr[j]
        if result == S:
            cnt += 1
    # print(cnt)

    print(f"#{t} {cnt}")