for t in range(1,int(input())+1):
    cnt = list(map(int, input().split())) 
    
    C = list(map(int, input().split())) #Containner
    T = list(map(int, input().split())) #Truck

    C.sort(reverse=True)
    T.sort(reverse=True)
    
    res = 0
    
    if len(C) > len(T): # Containner 수가 더 많을 경우
        idx = 0
        for i in range(len(T)):
            if C[idx] <= T[i]:
                res += C[idx]
                idx += 1
    else: #Truck 수가 더 많거나 같을 경우
        idx = 0
        for i in range(len(C)):
            if C[i] <= T[idx]:
                res += C[i]
                idx += 1
    print("#"+str(t), res)