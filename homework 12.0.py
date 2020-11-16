# Ruben
# 1
def rotateImage(a):
    matrix = [[] for _ in range(len(a))]
    for i in range(len(a)-1, -1, -1):
        for j in range(len(a)-1, -1, -1):
            matrix[i].append(a[j][i])
    print(matrix)
    return matrix

# 2
def digitsProduct(product):
    digits = []
    if product == 0: return 10
    if product == 1: return 1
    for i in range(9, 1, -1):
        while(product%i == 0):
            digits.append(str(i))
            product /= i
    if digits != [] and int(''.join(digits)) > int(''.join(digits[::-1])):
        digits = digits[::-1]
    print(f'product : {product}')
    if product > 1:
        return -1
    return int(''.join(digits))
