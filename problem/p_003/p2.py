"""
# 영어 이름 출력하기 

> 영어 이름은 가운데 이름을 가지고 있는 경우가 있습니다.

> 가운데 이름은 축약해서 나타내는 함수를 작성해보세요.

예시 입력)
Alice Betty Catherine Davis

예시 출력)
Alice B. C. Davis
"""

name = input()
# 아래에 코드를 작성하세요.
data = name.split(" ")

result = list()
for i in data:
    if i==data[0] or i==data[-1]:
        result.append(i)
    else:
        result.append(f"{i[0]}.")

result = " ".join(result)
print(result)
