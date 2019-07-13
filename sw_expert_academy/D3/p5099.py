import sys
sys.stdin = open('../input/p5099.txt', 'r')

res = []
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = list(range(1,M+1))
    que = []
    idx_que = []

    for i in range(N):
        que.append(arr.pop(0))
        idx_que.append(idx.pop(0))

    while len(idx_que) > 0:
        pizza = que.pop(0)//2
        index = idx_que.pop(0)

        if pizza == 0:
            if len(arr) > 0:
                que.append(arr.pop(0))
                idx_que.append(idx.pop(0))
        else:
            que.append(pizza)
            idx_que.append(index)

    res.append(index)

for i in range(len(res)):
    print("#{} {}".format(i+1, res[i]))
