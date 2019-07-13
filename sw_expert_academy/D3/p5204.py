def merge(a):
    global cnt
    if len(a)==1:
        return a
    else:
        m = len(a)//2
        left = a[:m]                # 리스트 왼쪽 절반
        right = a[m:]               # 오른쪽 절반
        left = merge(left)              # 정렬된 리스트 리턴
        right = merge(right)            # 정렬된 리스트 리턴
        idxl = 0
        idxr = 0
        i = 0
        while idxl<len(left) and idxr<len(right):  # 좌 우 리스트에서 비교 대상이 남은 경우
            if left[idxl]<right[idxr]:
                a[i] = left[idxl]
                idxl += 1
            else:
                a[i] = right[idxr]
                idxr += 1
            i += 1
        if left[-1]>right[-1]:     # 왼쪽 마지막 원소가 큰 경우
            cnt += 1
        if idxl<len(left):       # 왼쪽 리스트가 남은 경우
            a[i:] = left[idxl:]
    
        if idxr<len(right):    # 오른쪽 리스트가 남은 경우
            a[i:] = right[idxr:]
        return a                    # 왼쪽 오른쪽을 합쳐 정렬된 리스트 반환

res = []
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = merge(A)
    res.append('#{} {} {}'.format(tc, A[N//2], cnt))

for i in range(len(res)):
    print(res[i])