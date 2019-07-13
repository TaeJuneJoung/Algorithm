def bfs(arr, i, j, cnt):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    q = []
    q.append(i)
    q.append(j)
    while q:
        arr[i][j] = 1
        x = q.pop()
        y = q.pop()
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if arr[dx][dy] == 0:
                arr[dx][dy] = 1
                cnt += 1
                q.append(dx)
                q.append(dy)
            elif arr[dx][dy] == 3:
                return 1
    return 0


for t in range(10):
    T = input()
    arr = [0 for i in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input()))
    cnt = 1
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                print("#"+T, bfs(arr, i, j, cnt))