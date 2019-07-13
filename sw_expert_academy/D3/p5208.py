def f(n,k,e,c):
    global minV
    if n == k:
        if minV > c:
            minV = c
    elif minV <= c:
        return
    else:
        if e > 0:
            f(n+1, k, e-1, c)
        f(n+1, k, M[n]-1, c+1)

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = arr[1:]
    minV = 10005
    f(1,N-1,M[0]-1,0)
    print("#{} {}".format(t,minV))