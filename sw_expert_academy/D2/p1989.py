import sys
sys.stdin = open('../input/p1989.txt', 'r')

T = int(input())
for t in range(1,T+1):
    ent = input()
    result = 1
    for i in range(len(ent)//2):
        if ent[i] != ent[len(ent)-i-1]:
            result = 0
            break

    print(f"#{t} {result}")