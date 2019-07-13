import sys
sys.stdin = open('../input/p1213.txt', 'r', encoding='UTF8')

"""
T - 테스트케이스 번호 담는 변수
findStr - 찾는 문자를 담는 변수
enterStr - 입력 문자를 담는 변수

start - 시작인덱스
end - enterStr의 길이
k - findStr의 길이

resultStr - 슬라이싱한 값을 담는 변수
count - 카운트 변수

[주의할점]
#끝나는 인덱스 처리
TestCase 10번 문제와 같은 경우
"""

for t in range(1,11):
    T = input()
    findStr = input()
    enterStr = input()
    start = 0
    end = len(enterStr)
    k = len(findStr)
    count = 0
    while start < end-k+1 :
        resultStr = ""
        for i in range(k):
            resultStr += enterStr[start+i]
        if resultStr == findStr:
            count += 1
        start += 1
    print(f"#{t} {count}")