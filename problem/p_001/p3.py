"""
[개굴개굴 개구리]
"개굴!"
인간의 언어가 "개굴"이라고 표현됨

임의의 길이의 문자열을 입력시 그 길이만큼 "개굴"을 출력하도록 하세요.
단, 공백은 그대로 유지되어야 합니다.

ex)
    입력 예시 :
        안녕 나는 파이썬이야
    
    결과 예시 :
        개굴개굴 개굴개굴 개굴개굴개굴개굴개굴
"""

inputValue = input()
inputSplit = inputValue.split(" ")

for i in inputSplit:
    a = len(i)
    print("개굴"*a, end=' ')
result = ""


'''
# 다른방도
'''
# inputValue = input()
# for i in inputValue:
#     if i==" ":
#         result += i
#     else:
#         result += "개굴"
# print(result)
