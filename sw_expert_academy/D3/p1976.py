import sys
sys.stdin = open("../input/p1976.txt","r")

T = int(input())
for t in range(1,T+1):
    H1, M1, H2, M2 = map(int, input().split())
    if M1 + M2 >= 60:
        H1 += 1
    M1 = (M1 + M2)%60
    H1 = H1 + H2
    if H1 > 12:
        H1 = H1 - 12
    print(f"#{t} {H1} {M1}")

#Short 코딩 & 더 빠름
# for t in range(int(input())):
#     h1, m1, h2, m2 = map(int, input().split())
#     print(f'#{t+1} {((h1+h2)%12)+(m1+m2)//60 or 12} {(m1+m2)%60}')