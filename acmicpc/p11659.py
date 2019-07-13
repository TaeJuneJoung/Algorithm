"""
동일한 데이터에 접근하는 횟수가 여러번이므로
먼저 값을 저장해놓고 여러번 접근하는 방법이 시간 효율성이 있음.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

value = [0 for i in range(N+1)]
for i in range(N):
    value[i+1] = nums[i] + value[i]

for m in range(M):
    a, b = map(int, input().split())
    if a > 0:
        print(value[b]-value[a-1])
    else:
        print(value[b])