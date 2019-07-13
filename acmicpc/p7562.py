def bfs(visited, i,j, cnt):
    di = [1, 2, 2, 1, -1, -2, -2, -1]
    dj = [2, 1, -1, -2, -2, -1, 1, 2]
    q = []
    q.append(i)
    q.append(j)
    while q:
        x = q.pop(0)
        y = q.pop(0)
        if x == end_point[0] and y == end_point[1]:
            return visited[x][y]
        for k in range(len(di)):
            dx = x + di[k]
            dy = y + dj[k]
            if 0 <= dx < N and 0 <= dy < N:
                if visited[dx][dy] == 0:
                    visited[dx][dy] = visited[x][y] + 1
                    q.append(dx)
                    q.append(dy)
    return 0

T = int(input())
for t in range(T):
    N = int(input()) #체스판의 크기
    start_point = list(map(int, input().split()))
    end_point = list(map(int, input().split()))
    visited = [[0 for i in range(N)] for i in range(N)]
    cnt = 0
    print(bfs(visited, start_point[0],start_point[1], cnt))