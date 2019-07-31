di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def bfs(i, j, cnt):
    q = []
    visited = [[0]*col for i in range(row)]
    q.append(i)
    q.append(j)
    visited[i][j] = 1
    while len(q) != 0:
        i = q.pop(0)
        j = q.pop(0)
        for k in range(4):
            dx = i + di[k]
            dy = j + dj[k]
            if dx >= 0 and dy >= 0 and dx < row and dy < col:
                if(M[dx][dy] == 2):
                    return visited[i][j] +1
                if M[dx][dy] == 1 and visited[dx][dy] == 0:
                    q.append(dx)
                    q.append(dy)
                    visited[dx][dy] = visited[i][j] + 1
    return 0

row, col = map(int, input().split())
M = [0] * row

for i in range(row):
    M[i] = list(map(int, input()))
M[row-1][col-1] = 2
print(bfs(0, 0, 0))
