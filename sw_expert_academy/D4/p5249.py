def make_set(x):
    p[x] = x

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x,y):
    p[find_set(y)] = find_set(x)

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    p = [0]*(N+1)
    for i in range(N+1):
        make_set(i)

    arr = [list(map(int, input().split())) for i in range(M)]
    arr.sort(key=lambda i:i[2])

    nums = 0
    for i in range(M):
        if find_set(arr[i][0]) != find_set(arr[i][1]):
            nums += arr[i][2]
            union(arr[i][0], arr[i][1])
    print("#{} {}".format(t, nums))