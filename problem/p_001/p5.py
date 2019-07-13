"""
[개구리 왕자 이름 찾기]
수많은 개구리 중 이름이 F로 시작하는 개구리 왕자 찾기
(단, 개구리들은 개성이 넘쳐서 이름과 시작하는 알파벳이 다릅니다.)

문자열이 여러개 담긴 리스트 frogList가 매개변수로 주어졌을 때,
문자열이 'F'로 시작하면 그 이름을 return 하도록 isPrince()함수를 작성했습니다.
그러나, 코드 일부분이 잘못되어 있기 때문에 코드가 올바르게 동작하지 않습니다.
주어진 코드를 변경해서 올바르게 동작하도록 수정하세요.

frogList에는 반드시 F로 시작하는 이름이 하나 들어있습니다.

ex)
    isPrince(['Alice','Bob','Frog'])

    반환값 : Frog
"""

frogList = ['Alice','Bob','Frog']

def isPrince(frogList):
    for i in frogList:
        if(i[0].upper()=='F'):
            return i

print(isPrince(frogList))
