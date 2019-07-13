def f(n,k,l,r,ld,rd):
    if r > l:
        return 0
    if n == k:
        return 1
    elif d[ld][rd] != -1:
        return d[ld][rd]
    else:
        cnt = 0
        for i in range(N):
            if u[i] == 0:
                u[i] = 1
                cnt += f(n+1, k, l+M[i], r, ld+(1<<i),rd)
                cnt += f(n+1, k, l, r+M[i],ld,rd+(1<<i))
                u[i] = 0
        d[ld][rd] = cnt
        return cnt
    
T = int(input())
for t in range(1,T+1):
    N = int(input())
    M = list(map(int, input().split()))
    u = [0]*N
    d = [[-1]*(2**N) for i in range(2**N)] #-1이면 확인을 안해본것
    
    print("#{} {}".format(t,f(0,N,0,0,0,0)))