def change(money, cnt, max_change, change_list):
    while len(change_list) < 8:
        if cnt == 0:
            M = money // max_change
            money -= M * max_change
            max_change = max_change // 5
            cnt = 1
            change_list.append(M)
            change(money, cnt, max_change, change_list)
        else:
            M = money // max_change
            money -= M * max_change
            max_change = max_change // 2
            cnt = 0
            change_list.append(M)
            change(money, cnt, max_change, change_list)
    return change_list

res = []
T = int(input())
for t in range(T):
    value = change(int(input()), 0, 50000, [])#cnt가 0일때는 앞자리가 5일 때
    res_str = ""
    for i in range(len(value)):
        if i != len(value)-1:
            res_str += str(value[i]) + " "
        else:
            res_str += str(value[i])
    res.append(res_str)

for i in range(len(res)):
    print("#{}".format(i+1))
    print(res[i])