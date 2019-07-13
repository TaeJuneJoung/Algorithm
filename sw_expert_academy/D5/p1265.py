for t in range(1, int(input())+1):
    N, P = map(int, input().split())
    pocket = [N//P for i in range(P)]
    res = 1
    for i in range(N%P):
        pocket[i] += 1

    for i in range(P):
        res *= pocket[i]

    print("#{} {}".format(t, res))