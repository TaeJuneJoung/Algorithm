import sys
sys.stdin = open('../input/p4865.txt', 'r')

T = int(input())
for t in range(1,T+1):
    str1 = input()
    str2 = input()
    data = []
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
        data.append(cnt)

    res = data[0]
    for i in range(len(data)-1):
        res = res if res>data[i] else data[i]
    print(data)
    print(f"#{t} {res}")