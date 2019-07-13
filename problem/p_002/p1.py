"""
조건문을 통해 변수 score에 따른 평점을 출력하세요.

점수      등급
95점 이상   A+
90점 이상   A
85점 이상   B+
80점 이상   B
75점 이상   C+
70점 이상   C
65점 이상   D+
60점 이상   D
60점 미만   F
"""

score = int(input("점수를 입력하세요 : "))

if(score//10>=9):
    print("A", end="")
    if(score>=95):
        print("+")
elif(score//10>=8):
    print("B", end="")
    if(score%10>=5):
        print("+")
elif(score//10>=7):
    print("C", end="")
    if(score>=75):
        print("+")
elif(score//10>=6):
    print("D", end="")
    if(score>=65):
        print("+")
else:
    print("F")
    