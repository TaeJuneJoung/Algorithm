"""
# 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

예시 입력)
'Life is too short, you need python'

예시 출력)
Lf s t shrt, y nd pythn

"""

enterData = input()
collection = ['a','e','o','i','u']
result = list()
for i in enterData:
    if i.lower() not in collection:
        result.append(i)
    else:
        pass
result = "".join(result)
print(result)
