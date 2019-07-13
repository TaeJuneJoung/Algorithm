"""
[1859.백만 장자 프로젝트]
거꾸로 접근하면 쉽게 풀린다.
"""
T = int(input())
for t in range(1, T+1):
    res = 0 #결과값
    N = int(input()) #N일
    arr = list(map(int, input().split())) #각일마다 가격
    
    # arr.reverse() #reverse를 이용하여 반복문을 정방향으로 진행하여도 됨
    # max_value = arr[0] #값을 담는 함수

    #거꾸로 접근
    max_value = arr[-1] #값을 담는 함수
    for i in range(N-2,-1,-1):
        if max_value > arr[i]:
            res += max_value - arr[i]
        else:
            max_value = arr[i]
    
    print("#{} {}".format(t, res))