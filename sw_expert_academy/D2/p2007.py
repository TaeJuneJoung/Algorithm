T = int(input())
for t in range(1, T+1):
    M = input()
    for i in range(1,len(M)):
        if M[:i] == M[i:2*i]:
            res = M[:i]
            break

    print('#{} {}'.format(t, len(res)))