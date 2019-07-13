for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count_list = [0] * N
    for i in range(M):
        for a in range(N):
            if B[i] >= A[a]:
                count_list[a] += 1
                break
    max_value = 0
    max_idx = 0
    for i in range(N):
        if count_list[i] > max_value:
            max_value = count_list[i]
            max_idx = i
 
    print("#{} {}".format(t,max_idx+1))