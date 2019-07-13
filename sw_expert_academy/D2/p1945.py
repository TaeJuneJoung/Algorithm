for t in range(1,int(input())+1):
    N = int(input())
    num=[2,3,5,7,11]
    a=b=c=d=e=0
    while N > 1:
        if N%num[4] == 0:
            N = N//num[4]
            e += 1
        elif N%num[3] == 0:
            N = N//num[3]
            d += 1
        elif N%num[2] == 0:
            N = N//num[2]
            c += 1
        elif N%num[1] == 0:
            N = N//num[1]
            b += 1
        else:
            N = N//num[0]
            a += 1
    print("#"+str(t),a,b,c,d,e)