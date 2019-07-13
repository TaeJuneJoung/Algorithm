for t in range(1,int(input())+1):
    N = int(input())
    M = [list(map(int, input().split())) for i in range(N)]

    M.sort(key=lambda i:i[0])
    M.sort(key=lambda i:i[1])

    end = 0
    cnt = 0
    for i in range(N):
        if M[i][0] >= end:
            end = M[i][1]
            cnt += 1

    print("#"+str(t), cnt)