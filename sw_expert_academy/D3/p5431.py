import sys
sys.stdin = open("../input/p5431.txt", "r")

T=int(input())
for t in range(T):
    N,K=map(int, input().split())
    print(f"#{t+1} {' '.join(map(str,set(range(1,N+1))-set(map(int, input().split()))))}")