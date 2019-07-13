import sys
sys.stdin = open('../input/p1959.txt', 'r')

for t in range(1, int(input())+1):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_num = 0

    if a >= b:
        for i in range(a-b+1):
            num = 0
            for j in range(b):
                num += A[i+j] * B[j]
            max_num = num if num > max_num else max_num

    else: # a < b
        for i in range(b-a+1):
            num = 0
            for j in range(a):
                num += B[i+j] * A[j]
            max_num = num if num > max_num else max_num

    print("#"+str(t)+" "+str(max_num))