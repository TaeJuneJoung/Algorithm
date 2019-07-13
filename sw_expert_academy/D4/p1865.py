def nPr(n, r, s):
    global maxV
    if n == r:
        if s > maxV:
            maxV = s
        else:
            return
    elif s <= maxV: #BackTracking 엄청난 차이를 일궈냄
        return
    else:
        for i in range(n):
            if used[i] == 0: #i번 일을 맡은 사람이 아직 없으면
                used[i] = 1 #i번 일이 배정되었음을 기록
                nPr(n, r+1, s*M[r][i]) #n번 사람이 i번 일을 하는데 걸리는 시간 추가, n+1 사람의 일을 배정하러 이동
                used[i] = 0 #i번 일이 다른 사람에게 배정할 수 있도록 풀어줌

res = []
T = int(input())
for t in range(1,T+1):
    N = int(input())
    M = [list(map(int,input().split())) for i in range(N)]
    for i in range(N):
        for j in range(N):
            M[i][j] = M[i][j]/100
    used = [0] * N #배정된 일은 1로 표시
    maxV = 0
    nPr(N, 0, 1)
    maxV *= 100
    res.append("#"+str(t)+" "+"%0.6f" %maxV)

for i in range(len(res)):
    print(res[i])