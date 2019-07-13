res = []
for t in range(1,int(input())+1):
    N = int(input())
    M = []
    cnt_list = [[0 for i in range(10)] for i in range(10)]
    for i in range(N):
        M.append(list(map(int, input().split())))
    
    for i in range(N):
        for j in range(M[i][0], M[i][2]+1):
            for k in range(M[i][1], M[i][3]+1):
                cnt_list[j][k] += 1

    cnt = 0
    for i in range(10):
        for j in range(10):
            if cnt_list[i][j] == 2:
                cnt += 1

    res.append("#"+str(t)+" "+str(cnt))

for i in range(len(res)):
    print(res[i])