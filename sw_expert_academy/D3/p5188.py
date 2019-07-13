T = int(input())
for t in range(1,T+1):
    N = int(input())
    db = [[0 for i in range(N)] for i in range(N)]
    arr = [list(map(int, input().split())) for i in range(N)]

    db[0][0] = arr[0][0]
    idx = 0
    for i in range(1,N):
        db[i][0] = db[i-1][0] +arr[i][0]
        db[0][i] = db[0][i-1] + arr[0][i]

    for i in range(1,N):
        for j in range(1,N):
            right = db[i][j-1] + arr[i][j]
            down = db[i-1][j] + arr[i][j]
            db[i][j] = right if right < down else down
    print("#"+str(t),db[-1][-1])