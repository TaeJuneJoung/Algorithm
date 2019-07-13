import sys
sys.stdin = open('../input/p1208.txt', 'r')

for t in range(1,11):
    D = int(input())
    I = list(map(int, input().split()))
    for d in range(D):
        max_n = 0
        min_n = 101
        max_idx = 0
        min_idx = 0
        for i in range(100):
            temp = I[i]
            if min_n > temp:
                min_n = temp
                min_idx = i
            if max_n < temp:
                max_n = temp
                max_idx = i
        I[min_idx] += 1
        I[max_idx] -= 1
    print(f"#{t} {max(I) - min(I)}")
    
    # for i in range(100):
    #     temp = I[i]
    #     if min_n >= temp:
    #         min_n = temp
    #         min_idx = i
    #     if max_n <= temp:
    #         max_n = temp
    #         max_idx = i

    # print(f"#{t} {I[max_idx] - I[min_idx]}")
