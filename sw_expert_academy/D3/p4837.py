import sys
sys.stdin = open('../input/p4837.txt', 'r')

T = int(input())
A = list(range(1,13))

for t in range(1,T+1):
    N, K = list(map(int,input().split()))

    def find(arr, N):
        count = 0
        for i in range(1<<12):
            s = 0
            n_len = 0
            for j in range(12):
                if(i & (1 << j) != 0):
                    s += arr[j]
                    n_len += 1
            if(s == K and n_len == N):
                count += 1
        return count

    print(f"#{t} {find(A, N)}")