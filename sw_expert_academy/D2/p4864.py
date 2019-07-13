import sys
sys.stdin = open('../input/p4864.txt', 'r')

T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    res = 0
    for i in range(len(str2)-len(str1)+1):
        k = ""
        for j in range(len(str1)):
            k += str2[i+j]
        if k == str1:
            res = 1
            break

    print(f"#{t} {res}")