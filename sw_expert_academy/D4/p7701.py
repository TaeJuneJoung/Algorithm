
T = int(input())
for t in range(1,T+1):
    M = []
    for n in range(int(input())):
        M.append(input())
    #중복제거
    M = list(set(M))
    #길이, 사전순으로 정렬
    M.sort(key=lambda i:(len(i),i))
    print("#{}".format(t))
    for m in M:
        print(m)