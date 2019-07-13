for t in range(1, int(input())+1):
    N = int(input())
    M = list(map(int, input().split()))
    M.sort()
    print("#{} {}".format(t, M[N//2]))