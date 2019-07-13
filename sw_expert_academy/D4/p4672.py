T = int(input())
for t in range(1,T+1):

    N = list(input())
    N.sort() #정렬되어있을때 최대개수의 팰린드롬이 나오기에

    M = []
    for i in range(len(N)):
        for j in range(i,len(N)):
            M.append(N[i:j+1])
    cnt = 0
    for i in range(len(M)):
        if M[i][:] == M[i][-1::-1]:
            cnt += 1
        
    print("#{} {}".format(t, cnt))