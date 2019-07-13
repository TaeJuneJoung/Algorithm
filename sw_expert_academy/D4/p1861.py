di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(i,j,cnt):
    q = []
    q.append(i)
    q.append(j)
    while q:
        x = q.pop(0)
        y = q.pop(0)
        for k in range(len(di)):
            dx = x + di[k]
            dy = y + dj[k]
            if 0 <= dx < N and 0 <= dy < N:
                if arr[dx][dy] == arr[x][y]+1:
                    cnt += 1
                    q.append(dx)
                    q.append(dy)
    return cnt

T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]

    num = [0 for i in range(N**2+1)]
    max_cnt = 0
    idx = 0
    for i in range(N):
        for j in range(N):
            cnt = 1
            temp = bfs(i,j,cnt)
            num[arr[i][j]] = temp
            if max_cnt < temp:
                max_cnt = temp
    
    for i in range(len(num)):
        if num[i] == max_cnt:
            idx = i
            break
                
    print("#{} {} {}".format(t, idx, max_cnt))