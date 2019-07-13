import sys

N = int(sys.stdin.readline())
k = 0
nums = []
for i in range(N//(k+1)):
    if 6*k+1 >= N:
        break
    else:
        k += i
        nums.append(6*k+1)
if N == 1:
    print(1)
else:
    print(len(nums))

# # 방법2
# N = int(sys.stdin.readline())
# count = 0
# num = 1
# idx_list = [1]
# while num < N:
#     count += 6
#     num += count
#     idx_list.append(num)
# print(len(idx_list))


# # 처음과 같은 방도
# N = int(input())
# k = (N-2)//6
# num = 0
# res = 0
# for i in range(N//6+1):
#     num += i
#     if k < num:
#         res = i+1
#         break

# print(res)