import sys
sys.stdin = open('../input/p4843.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    M = list(map(int, input().split()))
    idx = 0
    for i in range(N):
        num = M[i]
        for j in range(i,N):
            if i%2==0:
                if M[j] >= num:
                    num = M[j]
                    idx = j
            else:
                if M[j] <= num:
                    num = M[j]
                    idx = j
        M[i],M[idx] = M[idx],M[i]
    result = ""
    for m in range(10):
        result += str(M[m])
        if m != N-1: #마지막 나오지 않게
            result += " "
    print(f"#{t} {result}")