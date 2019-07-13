import sys
sys.stdin = open('../input/p1961.txt', 'r')

T = int(input())
angle = 3
for t in range(1,T+1):
    N = int(input())
    arr = [0 for i in range(N)]
    copy_arr = [[0 for j in range(N)] for i in range(N)]
    row = ["" for i in range(N)]

    for n in range(N):
        arr[n] = list(map(int, input().split()))

    for a in range(angle):
        for i in range(N):
            for j in range(N):
                copy_arr[j][N-1-i] = arr[i][j]
        for i in range(N):
            for j in range(N):
                arr[i][j] = copy_arr[i][j]
        for i in range(N):
            for j in range(N):
                row[i] += str(arr[i][j])
            row[i] += " "

    print(f"#{t}")
    for i in range(N):
        print(row[i])