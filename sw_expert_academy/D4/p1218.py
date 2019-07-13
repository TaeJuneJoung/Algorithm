import sys
sys.stdin = open('../input/p1218.txt', 'r')

for t in range(1,11):
    N = int(input())
    enter = input()
    open_list = [0,0,0,0]
    close_list = [0,0,0,0]
    open_list[0] = enter.count('(')
    open_list[1] = enter.count('[')
    open_list[2] = enter.count('{')
    open_list[3] = enter.count('<')

    close_list[0] = enter.count(')')
    close_list[1] = enter.count(']')
    close_list[2] = enter.count('}')
    close_list[3] = enter.count('>')

    if open_list[0] == close_list[0] and open_list[1] == close_list[1] and open_list[2] == close_list[2] and open_list[3] == close_list[3]:
        result = 1
    else:
        result = 0
    print(f"#{t} {result}")