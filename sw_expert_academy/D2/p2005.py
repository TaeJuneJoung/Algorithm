T = int(input())
for t in range(1,T+1):
    N = int(input())
    angle = [[0 for i in range(j+1)] for j in range(N)]

    angle[0][0] = 1

    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                angle[i][j] = 1
            else:
                angle[i][j] = angle[i-1][j-1] + angle[i-1][j]

    print("#{}".format(t))
    for i in range(N):
        for j in range(i+1):
            print(angle[i][j], end=" ")
        print()