순열과 조합 공부
```python
"""
n:원소의 개수
k:현재까지 교환된 원소의 개수

arr:데이터의 저장된 배열
order:순열의 순서를 저장하는 리스트
"""

# def perm(order,k,n):
#     if n == k:
#         for i in range(N):
#             print(arr[order[i]], end=" ")
#         print()
#     else:
#         check = [False]*n
        
#         for i in range(k):
#             check[order[i]] = True

#         for i in range(n):
#             if check[i] == False:
#                 order[k] = i
#                 perm(order,k+1,n)

# N = int(input())
# arr = [1,2,3,4,5]
# order = [0 for i in range(len(arr))]
# perm(order,0,N)



def npr(n, k, p):  # 순열
    if n == k:
        print(p)
    else:
        for i in range(k, n):
            p[i], p[k] = p[k], p[i]
            npr(n, k+1, p)
            p[i], p[k] = p[k], p[i]


def ncr(n, r):  # 조합
    if r == 0:
        npr(len(tr), 0, tr)
    elif n < r:
        return
    else:
        tr[r-1] = a[n-1]
        ncr(n-1, r-1)
        ncr(n-1, r)


cnt = 0
a = [1, 2, 3, 4, 5]
R = 3
tr = [0]*R
ncr(len(a), R)
```

