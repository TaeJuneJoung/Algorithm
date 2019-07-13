T = int(input())
for t in range(1,T+1):
    N = list(map(int, input()))
    M = list(map(int, input()))
    temp = N[:]
    compare_list = []

    for i in range(len(N)):
        if N[i] == 1:
            N[i] = 0
        else:
            N[i] = 1
        compare_list.append(int("".join(map(str,N)),2))
        N = temp[:]
    # print(compare_list)

    temp = M[:]
    for i in range(len(M)):
        for j in range(2):
            if M[i] == 2:
                M[i] = 0
            else:
                M[i] += 1
            if int("".join(map(str,M)),3) in set(compare_list):
                print("#{} {}".format(t,int("".join(map(str,M)),3)))
        M = temp[:]