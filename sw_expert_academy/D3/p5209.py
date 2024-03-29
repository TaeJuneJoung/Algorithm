def nPr(n, r, s):
    global minV
    if n == r:
        if s < minV:
            minV = s
    elif s >= minV: #BackTracking 엄청난 차이를 일궈냄
        return
    else:
        for i in range(n):
            if used[i] == 0: #i번 일을 맡은 사람이 아직 없으면
                used[i] = 1 #i번 일이 배정되었음을 기록
                nPr(n, r+1, s+M[r][i]) #n번 사람이 i번 일을 하는데 걸리는 시간 추가, n+1 사람의 일을 배정하러 이동
                used[i] = 0 #i번 일이 다른 사람에게 배정할 수 있도록 풀어줌

T = int(input())
for t in range(1,T+1):
    N = int(input())
    M = [list(map(int,input().split())) for i in range(N)]
    used = [0] * N #배정된 일은 1로 표시
    minV = 10000005
    nPr(N, 0, 0)
    print("#"+str(t),minV)