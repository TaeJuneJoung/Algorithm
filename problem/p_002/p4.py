'''
다음은 학생들의 혈액형(A,B,O,AB)에 대한 데이터 이다.
for문을 활용하여 각 혈액형별 학생수를 구하세요
blood = ['A','B','O','A','B','A','AB','AB','O','A','O','AB','O']
'''

blood = ['A','B','O','A','B','A','AB','AB','O','A','O','AB','O']
blood_dict = dict()

for i in blood:
    if i in blood_dict:
        blood_dict[i] += 1
    else:
        blood_dict[i] = 1

print(blood_dict)
