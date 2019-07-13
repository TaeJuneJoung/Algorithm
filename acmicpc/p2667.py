import sys
sys.stdin = open('input/p2667.txt', 'r')

def bfs(arr, i, j, cnt):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    q = []
    q.append(i)
    q.append(j)
    arr[i][j] = 0
    while q:
        x = q.pop(0)
        y = q.pop(0)
        for k in range(4):
            dx = x + di[k]
            dy = y + dj[k]
            if 0 <= dx < N and 0 <= dy < N:
                if arr[dx][dy] == 1:
                    arr[dx][dy] = 0
                    cnt += 1
                    q.append(dx)
                    q.append(dy)
    return cnt

res = []
N = int(input())
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = list(map(int, input()))
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            res.append(bfs(arr, i, j, cnt))
res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])