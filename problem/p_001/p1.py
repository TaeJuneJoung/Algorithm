"""
[카드 병정의 장미 세기]
카드 병정들은 여왕의 명령에 따라 장미 숫자를 세기 시작했습니다.
"흰 장미 한개 ... 두개... 빨간 장미 한개..."

사칙연산을 이용해 장미의 숫자를 세봅시다.
+ - * /를 이용해 아래와 같은 값이 나오도록 빨간장미 x와 흰장미 y를 구해보세요

ex)
    my_sum = 9
    my_sub = 3
    my_mul = 18
    my_div = 2.0
    
"""

def my_sum(x,y):
    return x+y

def my_sub(x,y):
    return x-y

def my_mul(x,y):
    return x*y

def my_div(x,y):
    try:
        data = x/y
    except(ZeroDivisionError):
        print("분모는 0일 수 없습니다.")
        
    return data
    