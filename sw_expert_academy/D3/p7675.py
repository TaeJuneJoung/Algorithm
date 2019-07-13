"""
[통역사 성경이]
글에 쓰여있는데로 진행하면 됨
문자를 문장별로 나눠야하기에 나눈 후,
(문장의 기준은 '구두점')
1. 나눈 문장에서 첫번째 단어가 대문자인지 판별
2. 글자 길이가 1인지 판별 -> 이 부분을 간과하여 Fail 여러번 발생함
3. 문장에서 문자를 하나씩 보며
3-1. 숫자가 있는지 판별하고 있다면 다음 문장 판별로 Skip
3-2. 첫번째 문자 외에 대문자가 또 있다면 다음 문장 판별로 Skip
3-3. 이외에는 증가 요소로 두기
4. 구두점('.', '?', '!')가 나온다면 판별 idx를 하나 증가하여 문장별 증감에 맞게 표현
"""

T = int(input())
for t in range(1, T+1):
    N = int(input())
    data = input()
    nums = [0] * N
    idx = 0
    data = data.split()
    for value in data:
        isPlus = False
        if 65 <= ord(value[0]) <= 90:
            if len(value) == 1:
                isPlus = True
            for i in range(1, len(value)):
                if value[i].isdigit():
                    isPlus = False
                    break
                elif 65 <= ord(value[i]) <= 90:
                    isPlus = False
                    break
                else:
                    isPlus = True
        if isPlus:
            nums[idx] += 1
        if value[-1] == '.' or value[-1] == '?' or value[-1] == '!':
            idx += 1
    print('#{} {}'.format(t, ' '.join(map(str, nums))))