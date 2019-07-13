"""
최소공배수
"""
a = int(input("숫자, 입력값 :"))
b = int(input("숫자, 입력값 :"))

#최대공약수
def gcd(a, b):
    num = max(a, b)
    div = min(a, b)
    while num % div != 0:
        temp = num % div
        num = div
        div = temp
    return div

#최소공배수
def lcm(a, b):
    return (a * b) // gcd(a, b)