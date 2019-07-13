def check(count_list):
    for i in range(10):
        if count_list[i] == 3:
            return 1
        if i < 8:
            if count_list[i] >= 1 and count_list[i+1] >= 1 and count_list[i+2] >= 1:
                return 1
    return 0

for t in range(1, int(input())+1):
    cards = list(map(int, input().split()))

    count_list_A = [0 for i in range(10)]
    count_list_B = [0 for i in range(10)]
    res = "0"

    for card in range(len(cards)):
        if card % 2 == 1:
            count_list_B[cards[card]] += 1
        else:
            count_list_A[cards[card]] += 1
        if card >= 5:
            if check(count_list_A):
                res = "1"
                break
            if check(count_list_B):
                res = "2"
                break
    print("#"+str(t), res)