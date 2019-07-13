D = [[0]*141 for i in range(141)]

num = 1
num_cnt = 1
for i in range(len(D)):
    for j in range(num_cnt):
        D[i][j] = num
        num += 1
    num_cnt += 1

def idx_check(x,idx_num):
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] == x:
                idx[idx_num] = [i+1,j+1]
                return

T = int(input())
for t in range(1, T+1):
    a, b = map(int, input().split())
    idx = [0,0] #a, b - idx는 1번부터 시작한다고 가정
    idx_check(a,0)
    idx_check(b,1)
    
    cnt = 0
    
    x1 = idx[0][0]
    x2 = idx[1][0]
    y1 = idx[0][1]
    y2 = idx[1][1]

    while x1 != x2 or y1 != y2:
        if x1 == x2 and y1 == y2:
            break
        elif x1 > x2 and x1-x2 == y1-y2:
            x1 -= 1
            y1 -= 1
            cnt += 1
        elif x1 < x2 and x2-x1 == y2-y1:
            x1 += 1
            y1 += 1
            cnt += 1

        elif abs(x1-x2) < abs(y1-y2):
            if y1 > y2: # y>0이면
                y1 -= 1
                cnt += 1
            elif y1 < y2:
                y1 += 1
                cnt += 1
        else: # abs(x1-x2) > abs(y1-y2) 
            if x1 > x2:
                x1 -= 1
                cnt += 1
            elif x1 < x2:
                x1 += 1
                cnt += 1

    print("#{} {}".format(t, cnt))