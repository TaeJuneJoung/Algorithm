nums = [
    "0001101", "0011001", "0010011", "0111101", "0100011",
    "0110001", "0101111", "0111011", "0110111", "0001011"
    ]
ans_box = []
for t in range(1, int(input())+1):
    code = [0 for i in range(8)]

    num = ""
    rev_num = ""
    idx = 7
    isStart = False

    row, row_len = map(int, input().split())
    arr = [input() for i in range(row)]
    for i in range(row):
        for j in range(row_len-1, -1, -1):
            if len(rev_num) == 7:
                for k in range(6,-1,-1):
                    num += rev_num[k]
                code[idx] = num
                rev_num = ""
                num = ""
                isStart = False
                idx -= 1

            if arr[i][j] == '1':
                isStart = True

            if isStart and len(rev_num) < 7:
                rev_num += arr[i][j]

        if code[0] != 0:
            break

    decode = []
    for i in range(8):
        for j in range(10):
            if code[i] == nums[j]:
                decode.append(j)
                

    check = 0
    for i in range(len(decode)):
        if i%2:
            check += decode[i]
        else:
            check += decode[i] * 3

    res = 0
    if check%10 == 0:
        res = sum(decode) 
    else:
        res = 0

    ans_box.append("#{} {}".format(t, res))

for i in range(len(ans_box)):
    print(ans_box[i])