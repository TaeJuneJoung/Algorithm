def bfs(n,k):
    cnt = 0
    q = []
    q.append(n)
    v = [0]*(k+1)
    v[n] = 1
    while q:
        n = q.pop(0)
        cnt += 1
        for i in range(2, k+1):
            if adj[n][i] == 1 and v[i] == 0 and v[n] <= 2:
                q.append(i)
                v[i] = v[n] +1
    return cnt-1

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(M)]
    adj = [[0]*(N+1) for i in range(N+1)]
    for i in range(M):
        a = arr[i][0]
        b = arr[i][1]
        adj[a][b] = 1
        adj[b][a] = 1
    print("#{} {}".format(t,bfs(1,N)))