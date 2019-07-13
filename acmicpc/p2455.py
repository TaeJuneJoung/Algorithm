import sys
sys.stdin = open('input/p2455.txt', 'r')

# 방법1
# max_num = 0
# p_count = 0
# for station in range(4):
#     p_out, p_in = map(int, sys.stdin.readline().split())
#     p_count += p_in - p_out
#     if max_num < p_count:
#         max_num = p_count
# print(max_num)

#방법2
a = 0
result = exec('b,c=map(int,input().split());a=max(a,a+c-b);'*4)
print(a)