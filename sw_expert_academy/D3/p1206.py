import sys
sys.stdin = open('../input/p1206.txt', 'r')

for t in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(2,len(arr)-2):
        left = arr[i-1] if arr[i-1] > arr[i-2] else arr[i-2]
        right = arr[i+1] if arr[i+1] > arr[i+2] else arr[i+2]
        hight = left if left > right else right
        if arr[i] - hight > 0:
            sum += arr[i] - hight
    print(f"#{t} {sum}")

# # python스럽게
# for t in range(1,11):
#     N=int(input())
#     M=list(map(int,input().split()))
#     sum=0
#     for i in range(2,N-2):
#         b=max(M[i-2],M[i-1],M[i+1],M[i+2])
#         c=M[i]-b
#         if c>0:
#             sum+=c
#     print(f"#{t} {sum}")