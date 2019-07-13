def VLR(n):
    if n > 0:
        VLR(ch1[n]) #왼쪽 자식으로 이동
        print(arr[n], end="")
        VLR(ch2[n]) #오른쪽 자식으로 이동

def comVLR(n, k):
    if n <= k:
        comVLR(n*2, k) #완전이진트리 왼쪽자식
        print(arr[n], end="")
        comVLR(n*2+1, k) #완전이진트리 오른쪽자식

for t in range(1,11):
    N = int(input())
    ch1 = [0 for i in range(N+1)]
    ch2 = [0 for i in range(N+1)]
    arr = [0 for i in range(N+1)]
    for i in range(N):
        node = list(input().split())
        # if len(node) == 4:
        #     ch1[int(node[0])] = int(node[2])
        #     ch2[int(node[0])] = int(node[3])
        # elif len(node) == 3:
        #     ch1[int(node[0])] = int(node[2])
        # arr[int(node[0])] = node[1]
        arr[int(node[0])] = node[1]

    print("#"+str(t), end=" ")
    # VLR(1)
    comVLR(1,N)
    print()