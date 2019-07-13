"""
처음 시작이 1이면 cnt +1해주고,
그 다음 숫자가 이전 숫자와 같지 않으면 cnt +1
"""

T = int(input())
for t in range(1, T+1):
    N = input()
    if N[0] == '1':
        cnt = 1
    else:
        cnt = 0
    for i in range(1,len(N)):
        if N[i] != N[i-1]:
            cnt += 1
    print("#{} {}".format(t, cnt))