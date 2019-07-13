for t in range(1, int(input())+1):
    str_N = input().strip()
    cnt = 0
    while True:
        if len(str_N) > 2:
            str_N = str(int(str_N[0]) + int(str_N[1])) + str_N[2:]
            cnt += 1
        elif len(str_N) == 2:
            str_N = str(int(str_N[0]) + int(str_N[1]))
            cnt += 1
        else:
            break

    if cnt%2 == 0:
        print("#{} {}".format(t, "B"))
    else:
        print("#{} {}".format(t, "A"))