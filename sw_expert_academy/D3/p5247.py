def bfs(n, m):
    q = [0]*(1000001) #큐생성
    front = -1
    rear = -1
    visited = [0]*(1000001)
    
    rear += 1 #시작노드 인큐
    q[rear] = n
    visited[n] = 1 #시작노드 방문 표시
    
    while front != rear: #큐가 비어있지 않으면
        front += 1 #디큐
        n = q[front]
        if n == m:
            return visited[m] -1
        t = [n-10, n-1, n+1, n*2] #인접 노드번호 계산
        for i in range(len(t)):
            if t[i] > 0 and t[i] <= 1000000:
                if visited[t[i]] == 0:
                    visited[t[i]] = visited[n] +1
                    rear += 1
                    q[rear] = t[i]

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    print("#{} {}".format(t,bfs(N, M)))