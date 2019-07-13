"""
[1946.간단한 압축 풀기]
"""
T = int(input())
for t in range(1,T+1):
    N = int(input())
    res = ""
    
    for i in range(N):
        A, C = map(str, input().split())
        res += A*int(C)
    
    print("#"+str(t))
    cnt = 0
    for i in range(len(res)):
        if cnt == 10:
            cnt = 0
            print()
        cnt += 1
        print(res[i], end="")

    print()