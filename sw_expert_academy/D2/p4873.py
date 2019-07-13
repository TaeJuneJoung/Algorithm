import sys
sys.stdin = open('../input/p4873.txt', 'r')

res = []
T= int(input())
for t in range(T):
    enter = input()
    stack = [enter[0]]
    for i in range(1,len(enter)):
        if len(stack) == 0:
            stack.append(enter[i])
        elif stack[-1] == enter[i]:
            stack.pop()
        else:
            stack.append(enter[i])
    res.append(len(stack))
for i in range(len(res)):
    print(f"#{i+1} {res[i]}")