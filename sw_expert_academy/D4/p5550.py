import sys
sys.stdin = open('../input/p5550.txt', 'r')

def sound(frog):
    for i in range(len(frog)):
        if frog[i] == 'c':
            count_list[0] += 1
            if count_list[4] > 0:
                count_list[0] -= 1
                count_list[1] -= 1
                count_list[2] -= 1
                count_list[3] -= 1
                count_list[4] -= 1
        elif frog[i] == 'r':
            count_list[1] += 1
        elif frog[i] == 'o':
            count_list[2] += 1
        elif frog[i] == 'a':
            count_list[3] += 1
        elif frog[i] == 'k':
            count_list[4] += 1
        else:
            return -1

        for j in range(1,5):
            if count_list[j-1] < count_list[j]:
                return -1
    if count_list[0] == count_list[1] and count_list[0] == count_list[2] and count_list[0] == count_list[3] and count_list[0] == count_list[4]:
        return count_list[4]
    else:
        return -1

for t in range(1, int(input())+1):
    frog = input()
    count_list = [0 for i in range(5)]
    print("#"+str(t),sound(frog))