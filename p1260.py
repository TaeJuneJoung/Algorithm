def DFS(start):
    visited[start] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and arr[start][i] == 1:
            stack.append(i)
            DFS(i)
    return stack

def BFS(start):
    visited[start] = 1
    q = []
    q.append(start)
    while q:
        start = q.pop(0)
        if start > 0 and start < N+1:
            for i in range(1, N+1):
                if arr[start][i] == 1 and visited[i] == 0:
                    q.append(i)
                    visited[i] = 1
                    queue.append(i)
    return queue

N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

stack = [V]
visited = [0] * (N+1)
print(*DFS(V))

queue = [V]
visited = [0] * (N+1)
print(*BFS(V))