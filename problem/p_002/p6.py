'''
[별 찍기 - 반복문]
6-1
*****
****
***
**
*

6-2
*
**
***
****
*****

6-3
    *
   **
  ***
 ****
*****

6-4
*****
 ****
  ***
   **
    *

6-5
    *
   ***
  *****
 *******
*********

6-6
*********
 *******
  *****
   ***
    *

6-7
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
print("[6-1]")
num = 5
for i in range(5):
    for j in range(num):
        print("*", end="")
    num -= 1
    print()

print("[6-2]")
num = 1
for i in range(5):
    for j in range(num):
        print("*", end="")
    num += 1
    print()

print("[6-3]")
num = 4
for i in range(5):
    for j in range(5):
        if j >= num:
            print("*", end="")
        else:
            print(" ", end="")
    num -= 1
    print()

print("[6-4]")
num = 0
for i in range(5):
    for j in range(5):
        if j >= num:
            print("*", end="")
        else:
            print(" ", end="")
    num += 1
    print()

print("[6-5]")
num = 5
white = 4
for i in range(5):
    for j in range(num):
        if j < white:
            print(" ", end="")
        else:
            print("*", end="")
    num += 1
    white -= 1
    print()

print("[6-6]")
num = 9
white = 0
for i in range(5):
    for j in range(num):
        if j >= white:
            print("*", end="")
        else:
            print(" ", end="")
    num -= 1
    white += 1
    print()

print("[6-7]")
num = 5
white = 4
for i in range(9):
    if i < 4:
        for j in range(num):
            if j < white:
                print(" ", end="")
            else:
                print("*", end="")
        num += 1
        white -= 1
    else:
        for j in range(num):
            if j >= white:
                print("*", end="")
            else:
                print(" ", end="")
        num -= 1
        white += 1
    print()
    