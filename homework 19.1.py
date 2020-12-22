# Narek

def deg(n):
    degr = n if n < 10 else (n-9)*2+8
    num = 10 ** degr
    for i in range(2, n + 1):
        degr -= len(str(i))
        num += i*(10**degr)
    print(num)
deg(13)