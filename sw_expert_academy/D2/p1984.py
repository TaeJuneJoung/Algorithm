T = int(input())
for t in range(1, T+1):
    M = list(map(int, input().split()))
    M.sort()
    sum_val = 0
    for i in range(1, len(M)-1):
        sum_val += M[i]
    res = sum_val//(len(M)-2)
    res_float = sum_val/(len(M)-2) - sum_val//(len(M)-2)
    if res_float >= 0.5:
        res += 1
    print("#{} {}".format(t, res))