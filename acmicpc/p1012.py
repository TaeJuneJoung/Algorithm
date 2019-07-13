def bfs(arr, i, j, cnt):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    q = []
    q.append(i)
    q.append(j)
    while len(q) > 0:
        x = q.pop(0)
        y = q.pop(0)
        for d in range(4):
            dx = x + di[d]
            dy = y + dj[d]
            if 0 <= dx < N and 0 <= dy < M:
                if arr[dx][dy] == 1:
                    cnt += 1
                    arr[dx][dy] = 0
                    q.append(dx)
                    q.append(dy)
    return cnt

#i = N, j = M
for t in range(int(input())):
    res = []
    N, M, K = map(int, input().split())
    arr = [[0 for i in range(M)] for i in range(N)]

    for i in range(K):
        a, b = map(int,input().split())
        arr[a][b] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = 0
                res.append(bfs(arr, i, j, cnt+1))
    print(len(res))