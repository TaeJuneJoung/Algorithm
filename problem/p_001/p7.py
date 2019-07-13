"""
[별 헤는 밤]
주어진 조건(별의 거리)에 따라 달라지는 별을 출력하기

ex)
    3
    *   *   *
      *   *
    
    6
    *      *      *
        *     *    

별의 거리 i가 입력으로 주어질 때, 별 사이의 거리가 i인
W모양의 대칭인 별자리를 출력하세요

단, 별의 거리 i가 짝수이면 2행의 두 별 사이의 거리는 i-1

"""
star = "*"
white_space = " "

try:
  N = int(input())
  low2_w = 1
  low2_w = low2_w + int(N/2)
  print(low2_w)

  if(N%2==0):#짝수일때
    print((star+(white_space*N))*2+star)
    print(low2_w*white_space+star+white_space*(N-1)+star)
  else:#홀수일때
    print((star+(white_space*N))*2+star)
    print(low2_w*white_space+star+white_space*N+star)


    
except(ValueError):
  print("숫자를 넣어주세요")
