"""
month = 1~12을 담고 있는 range type 변수
day = 1~12월의 마지막 일수를 가지고 있는 list type 변수(단, 윤년 제외)
dict_date = 요일을 담고 있는 dict type 변수
index = 1년의 일수를 세며, 인덱싱을 위한 int type 변수
first_row = 한달의 첫째주를 판단하는 bool type 변수
arr = 달력을 담는 이중 list, list type 변수
"""

month = range(1,13)
day = [31,28,31,30,31,30,31,31,30,31,30,31]
dict_date = {
    0:"Su",
    1:"Mo",
    2:"Tu",
    3:"We",
    4:"Th",
    5:"Fr",
    6:"Sa"
}

index = 0
first_row = False
arr = list()

for m in month:
    print(f"{m} 월".center(20))
    print(" ".join(dict_date.values()))

    first_row = True

    for d in range(1,day[m-1]+1):
        arr.append([index,d])
        if index%7==0 and index/7 > 0 and first_row==False:
            print()

        if first_row:
            print(f"{'   '*(index%7)}", end="")
            first_row = False

        if d < 10 :
            print(f" {d} ", end="")
        else:
            print(f"{d} ", end="")
        index += 1
    print()
