'''
(QWERTY 키보드를 사용하여 타이핑을 한다고 가정할 때)
'편안한 단어'는 타이핑 할 때 손을 번갈아 칠 수 있는 단어를 말합니다.
단어를 인자로 받아 그것이 '편안한 단어'인지 여부를 True/False로 반환하는 함수를 만드세요.
(모든 단어는 a ~ z까지 오름차순으로 구성된 문자열입니다.)

문자 목록
왼손: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
오른손: y, u, i, o, p, h, j, k, l, n, m 


word = "jaja"
left, right = "qwertasdfgzxcvb","yuiophjklnm"

손을 번갈아서 치는 단어가 편안한 단어
한손에서 두 번이상 쳐야한다면 불편한 단어
'''


word = input("문장을 입력하여주세요 : ")
left, right = "qwertasdfgzxcvb","yuiophjklnm"
leftCount, rightCount = 0, 0
result = ""

for i in word:
    if i in left:
        leftCount += 1
    elif i in right:
        rightCount += 1
    if(abs(leftCount-rightCount)>=2):
        result = "불편한 단어"
        break
    else:
        result = "편한 단어"

print(result)
