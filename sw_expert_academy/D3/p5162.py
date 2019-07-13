for t in range(1, int(input())+1):
    A, B, C = map(int, input().split())
    print("#"+str(t), C//min(A,B))