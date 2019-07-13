def bfs(x, k):
    # 1~4 초기화
    # 1. 큐생성
    q = []
    # 2. visited생성
    visited = [0]*(100001)
    # 3. 인큐
    q.append(x)
    # 4. 시작점 방문 표시
    visited[x] = 1
    while(len(q) != 0):
        x = q.pop(0)
        if(x == k):
            return (visited[k] -1)
        # x-1이 인접이면서 방문하지 않았을 경우 // 무조건 x-1의 인접 확인이  앞에와야함
        if(x-1 >= 0 and visited[x-1] == 0):
            q.append(x-1)
            visited[x-1] = visited[x] + 1
        # x+1이 인접인 경우
        if(x+1 <= 100000 and visited[x+1] == 0):
            q.append(x+1)
            visited[x+1] = visited[x] + 1
        # 2*x 가 인접인 경우
        if(2*x <= 100000 and visited[2*x] == 0):
            q.append(2*x)
            visited[2*x] = visited[x] + 1
    return 0

x, k = map(int, input().split())
print(bfs(x, k))