import math


# Narek

def deg(n):
    degr = n if n < 10 else (n-9)*2+8
    num = 10 ** degr
    for i in range(2, n + 1):
        degr -= int(math.log10(i))+1
        num += i*(10**degr)
    print(num)
deg(16)
