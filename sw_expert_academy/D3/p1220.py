import sys
sys.stdin = open('../input/p1220.txt', 'r')

for t in range(1,11):
    N = int(input())
    x_list = [0 for i in range(N)]
    y_list = [0 for i in range(N)]
    for n in range(N):
        x_list[n] = list(map(int, input().split()))
    for n in range(N):
        y_list[n] = list(map(lambda i:i[n], x_list))

    isFN = 0
    isN = 0
    cnt = 0
    for i in range(N):
        isN = 0
        isFN = 0
        for j in range(N):
            if y_list[i][j] == 1:
                isN = 1
                isFN = 1
            if isFN == 1 and isN == 1 and y_list[i][j] == 2:
                cnt += 1
                isN = 0

    print(f"#{t} {cnt}")