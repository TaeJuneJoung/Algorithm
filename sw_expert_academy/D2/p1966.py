T = int(input())
for t in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    M.sort()
    print("#{} {}".format(t, " ".join(map(str, sorted(M)))))