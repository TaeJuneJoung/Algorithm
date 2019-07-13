res=[]
for t in range(1, int(input())+1):
    N = int(input())
    A, B = [], []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    C = []
    for i in range(P):
        C.append(int(input()))
    cnt = [0 for i in range(P)]

    for n in range(N):
        for c in range(len(C)):
            if A[n] <= C[c] <= B[n]:
                cnt[c] += 1

    str_res = "#"+str(t)+" "
    for i in range(len(cnt)):
        if i == P-1:
            str_res += str(cnt[i])
        else:
            str_res += str(cnt[i]) + " "
    res.append(str_res)
for i in range(len(res)):
    print(res[i])