M = [0 for i in range(1000001)]
for i in range(1,1000001,2): #홀수만 더하니 홀수만 체크
    for j in range(i, 1000001, i): #각 약수의 자리수를 더해주기 위해
        M[j] += i
 
#각 자리수를 더해줌
#시그마(3) = f(1) + f(2) +f(3)이므로
for i in range(1,1000000):
    M[i+1] += M[i]
 
res = []
T = int(input())
for t in range(1, T+1):
    L, R = map(int, input().split())
    L = L-1 #1을 빼줘야 해당 L은 포함하기에
    res.append("#{} {}".format(t, M[R]-M[L]))
     
for i in range(len(res)):
    print(res[i])