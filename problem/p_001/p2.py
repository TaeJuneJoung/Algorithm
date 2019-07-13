"""
[거꾸로 숫자 세기]
로켓 발사를 위해 거꾸로 숫자를 세는 코드를 작성해 보세요.
    1. count 10부터 시작
    2. 일단 count를 출력
    3. count를 -1 감소
    4. 2번과 3번을 10번 반복하세요
"""

count = 10
print(count)

for i in range(10,1,-1):
    count = count - 1
    print(count)
