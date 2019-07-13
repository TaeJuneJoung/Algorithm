import sys
sys.stdin = open('../input/p5549.txt', 'r')

res = []
T = int(input())
for t in range(T):
    N = int(input())
    if N%2 == 1:
        res.append("Odd")
    else:
        res.append("Even")

for i in range(len(res)):
    print(f"#{i+1} {res[i]}")