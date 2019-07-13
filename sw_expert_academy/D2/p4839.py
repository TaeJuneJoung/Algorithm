import sys
sys.stdin = open('../input/p4839.txt', 'r')

# T = int(input())
# for t in range(1,T+1):
#     r, a, b =map(int, input().split()) #r:총길이,a:A찾을페이지,b:B찾을페이지
#     r_a, r_b, l_a, l_b = r, r, 1, 1
#     c_a, c_b = (r_a+1)//2, (r_b+1)//2
#     cnt_a, cnt_b = 0, 0
#     winner = ""

#     while c_a != a:
#         if a > c_a:
#             l_a = c_a
#             c_a = (l_a+r_a)//2
#         else:
#             r_a = c_a
#             c_a = (l_a+r_a)//2
#         cnt_a += 1
    
#     while c_b != b:
#         if b > c_b:
#             l_b = c_b
#             c_b = (l_b+r_b)//2
#         else:
#             r_b = c_b
#             c_b = (l_b+r_b)//2
#         cnt_b += 1

#     if cnt_a < cnt_b:
#         winner = "A"
#     elif cnt_a == cnt_b:
#         winner = "0"
#     else:
#         winner ="B"

#     print(f"#{t} {winner}")


def binarySearch(all,point):
    l = 1
    c = (all+l)//2
    cnt = 0
    while c != point:
        if point > c:
            l = c
            c = (l+all)//2
        else:
            all = c
            c = (l+all)//2
        cnt += 1
    return cnt


T = int(input())
for t in range(1,T+1):
    r, a, b =map(int, input().split())
    a_team = binarySearch(r,a)
    b_team = binarySearch(r,b)
    result = ""
    if a_team < b_team:
        result = "A"
    elif a_team == b_team:
        result = "0"
    else:
        result = "B"
    print(f"#{t} {result}")