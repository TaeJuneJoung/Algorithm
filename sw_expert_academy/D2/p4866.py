import sys
sys.stdin = open('../input/p4866.txt', 'r')

T = int(input())
res = []
for t in range(T):
    enter = input()
    stack = []
    count = 0
    for i in range(len(enter)):
        if enter[i] == "{" or enter[i] == "(":
            stack.append(enter[i])
        elif enter[i] == "}":
            if len(stack) == 0:
                count += 1
                break
            elif stack[-1] == "{":
                stack.pop(-1)
            else:
                count += 1
                break
        elif enter[i] == ")":
            if len(stack) == 0:
                count += 1
                break
            elif stack[-1] == "(":
                stack.pop(-1)
            else:
                count += 1
                break
    if(count == 0 and len(stack) == 0):
        res.append(1)
    else:
        res.append(0)

for i in range(len(res)):
    print(f"#{i+1} {res[i]}")