"""
[1946.간단한 압축 풀기]
10개가 찍히면 다음줄로 내려가는 처리가 중요한 문제
또한, 테스트케이스가 하나 끝나면 한줄을 내려줘야한다

T : 테스트케이스
N : 받는 갯수
sum_num : 10개씩 띄어주기 위해서 사용
value : string타입의 값
num : value가 나오는 횟수
"""

T = int(input())
for t in range(1, T+1):
    print("#{}".format(t))
    N = int(input())
    sum_num = 0
    for i in range(N):
        value, num = map(str, input().split())
        num = int(num)
        for j in range(num):
            print(value, end="")
            sum_num += 1
            if sum_num == 10:
                sum_num = 0
                print()
    print()