"""
[토끼와 거북이의 달리기 경주]
토끼와 거북이가 달리기 경주를 시작
토끼는 N분에 한번 휴식
거북이는 M분에 한번 휴식

같이 쉬는 시간은 언제일까?

동시에 휴식하는 최초의 시간을 출력하는 프로그램 작성해보기

ex)
    3 5

    반환값 : 15
"""
print("시간을 띄어서 작성해주세요\n예를들어 : 3 5")

rest = input()

rest = rest.split(" ")
rabbitRest = int(rest[0])
turtleRest = int(rest[1])

#최소공배수 구하는 방법
# (a*b)/a와b의 최대공약수 -> 최소공배수

def lcm(x,y):#least common multiple
    while(y!=0):
        temp = x%y
        x = y
        y = temp
    return x

def gcd(x,y):#greatest common divisor
    result = x*y/(lcm(x,y))
    print(result)

gcd(rabbitRest,turtleRest)
