import sys
sys.stdin = open('../input/p1259.txt', 'r')

for t in range(1, int(input())+1):

    N = int(input())
    arr = list(map(int, input().split()))
    m_list = [] #숫나사 리스트
    w_list = [] #암나사 리스트
    for i in range(2*N):
        if i%2 == 0:
            m_list.append(arr[i])
        else:
            w_list.append(arr[i])

    res_list = [] #결과 리스트
    idx = 0 #pop을 위해 조건 성립 인덱스 저장 변수

    #처음 시작점을 잡기 위해 홀로 있는 나사를 찾는 작업 및 set변수를 int화
    first_screw = set(m_list)-set(w_list)
    first = 0
    for i in first_screw:
        first = i
    
    #처음 시작점 결과 리스트에 담기
    for i in range(N):
        if m_list[i] == first:
            idx = i
            break
    res_list.append(m_list.pop(idx))
    res_list.append(w_list.pop(idx))
    
    #처음 시작 암나사를 기준으로 맞춰나가는 작업
    while len(res_list) < 2*N:
        idx = 0
        for i in range(len(m_list)):
            if res_list[-1] == m_list[i]:
                idx = i
                break
        res_list.append(m_list.pop(idx))
        res_list.append(w_list.pop(idx))

    print("#"+str(t)+" "+" ".join(map(str,res_list)))