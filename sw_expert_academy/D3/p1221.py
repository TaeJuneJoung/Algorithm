import sys
sys.stdin = open('../input/p1221.txt', 'r')

# num_list = [0,1,2,3,4,5,6,7,8,9]
# num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# T = int(input())

# for t in range(T):

#     time, N = map(str, input().split())
#     N = int(N)
#     enter = list(map(str, input().split()))
    
#     for i in range(N):
#         for j in range(10):
#             if enter[i] == num[j]:
#                 enter[i] = num_list[j]

#     enter.sort()

#     for i in range(N):
#         for j in range(10):
#             if enter[i] == num_list[j]:
#                 enter[i] = num[j]

#     print(time)
#     print(" ".join(enter))

T=int(input())
L=["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
for i in range(T):
    t,M = input().split()
    n = input().split()
    print("\n"+t)
    for i in L:
        print((i+" ")*n.count(i),end=" ")