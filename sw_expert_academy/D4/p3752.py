T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    scores = [0]
    visited = [0]*(100*100+1)

    for i in range(N):
        for j in range(len(scores)):
            temp = arr[i]+scores[j]
            if visited[temp] == 0:
                visited[temp] = 1
                scores.append(temp)

    print("#{} {}".format(t, len(scores)))