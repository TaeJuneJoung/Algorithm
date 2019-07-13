'''
다음 딕셔너리에서 평균 점수를 구하세요<br>
student = {'python':80, 'algorithm':78, 'django':95, 'flask':80}
'''

student = {'python':80, 'algorithm':78, 'django':95, 'flask':80}
print("평균점수 : ",sum(student.values())/len(student))

#주의할점. 변수를 선언한다고 sum = 0을 해서 진행하면
#sum 메소드를 사용하는데 문제가 생김. -> 변수명으로 keylist의 값을 사용하지 말것!
