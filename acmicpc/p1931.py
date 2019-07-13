N = int(input())
M = [0 for i in range(N)]
for i in range(N):
    M[i] = list(map(int,input().split()))
M.sort(key=lambda i:i[0])
M.sort(key=lambda i:i[1])

meeting_time = []
end = 0
cnt = 0
for i in range(len(M)):
    if M[i][0] >= end : #앞의 회의가 끝난 후 시작하면
        end = M[i][1]
        meeting_time.append(M[i])
        cnt += 1
print(cnt)