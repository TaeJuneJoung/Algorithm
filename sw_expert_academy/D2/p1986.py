T = int(input())
for t in range(1,T+1):
    res = 0
    N = int(input())
    for i in range(1,N+1):
        if i%2:#홀수
            res += i
        else:
            res -= i
    print('#{} {}'.format(t, res))