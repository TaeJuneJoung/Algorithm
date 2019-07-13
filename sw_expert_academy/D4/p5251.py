def dij(s, V):
    u = set([s])

    for i in range(V+1):
        D[i] = arr[s][i]

    while len(u) != V:
        minV = 10001
        w = 0
        for i in range(V+1):
            if i not in u:
                if D[i] < minV:
                    minV = D[i]
                    w = i

        u.add(w)

        for i in range(V+1):
            if w != i and arr[w][i] != 10001:
                D[i] = min(D[i], D[w] + arr[w][i])
    

T = int(input())
for t in range(1,T+1):
    N, E = map(int, input().split())
    arr = [[10001]*(N+1) for i in range(N+1)]

    for i in range(N+1):
        arr[i][i] = 0

    for i in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = w
    s = 0
    D = [0]*(N+1)
    dij(s, N)
    print("#{} {}".format(t,D[N]))