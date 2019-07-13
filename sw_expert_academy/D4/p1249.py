T = int(input())

di = [0,1,0,-1]
dj = [1,0,-1,0]
def bfs(i,j,s):
    s = arr[i][j]
    visited[i][j] = 1
    q = []
    q.append(i)
    q.append(j)
    while q:
        x = q.pop(0)
        y = q.pop(0)
        for k in range(len(di)):
            dx = x + di[k]
            dy = y + dj[k]
            if 0<=dx<N and 0<=dy<N:
                if visited[dx][dy] == 0 or dp[dx][dy] > dp[x][y] + arr[dx][dy]:
                    visited[dx][dy] = 1
                    q.append(dx)
                    q.append(dy)
                    dp[dx][dy] = dp[x][y] + arr[dx][dy]


for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for i in range(N)]
    visited = [[0]*N for i in range(N)]
    dp = [[0]*N for i in range(N)] #2N-1범위 2N까지 설정해주면 됨
    minV = 10005
    s = 0
    bfs(0,0,s)
    print("#{} {}".format(t,dp[-1][-1]))
