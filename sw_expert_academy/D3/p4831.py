import sys
sys.stdin = open('../input/p4831.txt', 'r')

T = int(input())
for t in range(1,T+1):
    K, N, M = list(map(int,input().split()))
    L = [0] + list(map(int, input().split())) +[N]
    lenL = len(L) -1
    start = 0
    end = lenL
    count = 0
    while start < end :
        if L[end] - L[start] <= K:
            start = end
            end = lenL
            if start == end:
                break
            count += 1
        else:
            end -= 1
            if start == end:
                count = 0
                break
    print(f"#{t} {count}")