import sys
sys.stdin = open('../input/p1860.txt', 'r')

res = []
T = int(input())
for t in range(T):
    N, M, K = map(int, input().split()) #N: 사람수 M: 초 K: M초동안 만드는 갯수
    P = list(map(int, input().split())) #사람이 오는 초
    isTrue = 1
    P.sort()

    for i in range(N):
        #1초에 만드는 갯수를 각 사람에 따라 곱해준 후,
        #i를 통해서 사람 수의 효과를 나타냄
        if P[i]//M*K < i+1:
            isTrue = 0
            break
    if isTrue == 0:
        res.append("Impossible")
    else:
        res.append("Possible")

for i in range(len(res)):
    print("#{} {}".format(i+1,res[i]))


res = []
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    score = 0
    for i in range(K):
        score += arr[i]

    res.append(score)

for i in range(len(res)):
    print("#{} {}".format(i+1, res[i]))