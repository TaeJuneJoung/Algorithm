for t in range(1, int(input())+1):
    arr = [[] for i in range(15)]
    for i in range(5):
        temp = input()
        for j in range(len(temp)):
            arr[j].append(temp[j])
    res = ""
    for i in range(15):
        for j in range(len(arr[i])):
            res += arr[i][j]

    print("#"+str(t), res)