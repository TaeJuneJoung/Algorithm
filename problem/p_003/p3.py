"""
# 달력 출력하기

> 1월 1일 월요일부터 12월 31일까지 달력을 출력하세요.

예시 출력)
         1 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 
         2 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 

         3 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 
         4 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 

"""

month = range(1,13)
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
date = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

for i in month:
    print(f"{i} 월".center(20))
    print(" ".join(date))
    for j in range(1,month_day[i-1]+1):
        if(j%7==1 and j>7):
            print()
        if(j<10):
            print(f" {j}",end=" ")
        else:
            print(f"{j}",end=" ")
    print()
