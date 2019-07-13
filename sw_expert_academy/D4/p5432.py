for t in range(1, int(input())+1):
    arr = input()
    stick = []
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:#같은경우
            if arr[i] == "(": # ( (
                stick.append(1)
            else: # ) )
                stick.pop(-1)
                cnt += 1
        else:#다른경우
            if arr[i] == "(": # ( )
                cnt += len(stick)
                # print(cnt)
            else: # ) (
                pass

    print("#"+str(t), cnt)