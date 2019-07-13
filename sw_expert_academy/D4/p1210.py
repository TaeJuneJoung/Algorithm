import sys
sys.stdin = open('../input/p1210.txt', 'r')

for t in range(1,11):
    T = int(input())
    idx = 98
    end = 0
    arr = [0 for i in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    for i in range(100):
        if arr[99][i] == 2:
            end = i
    while idx != 0:
        if end > 0 and arr[idx][end-1] == 1:#왼쪽
            while end > 0 and arr[idx][end-1] == 1:
                end -= 1
            idx -= 1
        elif end < 99 and arr[idx][end+1] == 1:#오른쪽
            while end < 99 and arr[idx][end+1] == 1:
                end += 1
            idx -= 1
        else:
            idx -= 1

    print(f"#{t} {end}")