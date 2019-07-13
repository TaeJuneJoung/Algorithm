for t in range(1,int(input())+1):
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    bef_mon, bef_day, aft_mon, aft_day = map(int, input().split())
    sum_day = 0
    for i in range(aft_mon-bef_mon):
        sum_day += day[bef_mon+i-1]
    sum_day += aft_day - bef_day +1
    print("#"+str(t), sum_day)