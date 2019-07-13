"""
시간 효율을 위해 담고 접근하는 방식
"""

D = [0] * 1000001
D[1] = 1
D[2] = 2
D[3] = 4
for i in range(4,len(D)):
    D[i] = (D[i-1] + D[i-2] + D[i-3])%1000000009

for t in range(1, int(input())+1):
    N = int(input())
    print(D[N])