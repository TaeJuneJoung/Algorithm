M, N = map(int, input().split())
enter = [input() for i in range(M*5+1)]
res = [0 for i in range(5)]

for j in range(1,len(enter[0]), 5):#len(enter)+1
    cnt = 0
    for i in range(1,5*M+1):
        # print(enter[i][j], end=" ")
        if enter[i][j] == "*":
            cnt += 1
        elif enter[i][j] == "#":
            res[cnt] += 1
            cnt = 0

print(" ".join(map(str, res)))