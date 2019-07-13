import sys
sys.stdin = open('../input/p1209.txt', 'r')

#2차열 리스트가 아닌 하나의 리스트로 담아진행. But, 느림
for t in range(10):
    t_n = int(input())
    M = list()
    for m in range(100):
        array = list(map(int, input().split()))
        M.extend(array)
        d_x = sum(M[0::101])
        d_y = sum(M[99:9902:99])
        result = d_x if d_x > d_y else d_y
        for i in range(100):
            start = 100*i
            end = 100*(i+1)
            startCol = i
            row = sum(M[start:end])
            col = sum(M[startCol::100])
            result = row if row > result else result
            result = col if col > result else result
    print(f"#{t_n} {result}")


# 2019.02.25 풀이
# for t in range(1,11):
#     T = int(input())
#     arr = [list(map(int, input().split())) for i in range(100)]
#     left = 0
#     right = 0
#     num_val = 0
#     for i in range(100):
#         left += arr[i][i]
#         right += arr[i][i]
#         row_val = 0
#         col_val = 0
#         for j in range(100):
#             row_val += arr[i][j]
#             col_val += arr[j][i]
#         num_val = num_val if num_val > row_val else row_val
#         num_val = num_val if num_val > col_val else col_val

    
#     max_val = left if left > right else right
#     max_val = max_val if max_val > num_val else num_val

#     print(f"#{t} {max_val}")