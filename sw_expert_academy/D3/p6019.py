import sys
sys.stdin = open('../input/p6019.txt', 'r')

T = int(input())
for t in range(T):
    M, A, B, F = map(int, input().split())
    res = (M/(A+B))*F

    print(f"#{t+1} {res}")

# # 빠른 속도 풀이 : 이유 판별중
# res = []
# for i in range(int(input())):
#     l = list(map(int, input().split()))
#     res.append(str(format((l[0] / (l[1] + l[2])) * l[3], '.6f')))
# for i in range(len(res)):
#     print("#" + str(i + 1) + " " + res[i])