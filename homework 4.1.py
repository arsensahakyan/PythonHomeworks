# Narek
# 1
list = [5, 3, 6, 7, 9]
def minStep(list):
    min_step = 0
    for i in range(2, max(list)+1):
        f = True
        k = 0 + i - 1
        while k < list[0]:
            k += i
        for j in range(1, len(list) + 1):
            if k == sum(list[0:j]):
                print(list[j - 1] + list[j - 2])
                f = False
                break
            k += i
        print(f)
        if f:
            return i
        else:
            continue

print(minStep(list))

# 2
def equation(equ):
    ind = 1
    elems = []
    for i in range(1, len(equ)+1):
        if equ[i - 1] in '-=+':
            elems.append(equ[ind - 1:i - 1])
            ind = i

    xindex = 0
    numindex = 0
    for i in range(len(elems)):
        if 'x' in elems[i]:
            if elems[i][0:len(elems[i]) - 1].isdigit() or elems[i][1:len(elems[i]) - 1].isdigit() and elems[i][0] == '+':
                xindex += float(elems[i][0:len(elems[i]) - 1])
            elif elems[i][1:len(elems[i]) - 1].isdigit() and elems[i][0] == '-':
                xindex -= float(elems[i][1:len(elems[i]) - 1])
            elif elems[i] == 'x':
                xindex += 1
        else:
            if elems[i][0:len(elems[i])].isdigit() or elems[i][1:len(elems[i])] and elems[i][0] == '+':
                numindex += float(elems[i][0:len(elems[i])])
            elif elems[i][1:len(elems[i])] and elems[i][0] == '-':
                numindex -= float(elems[i][1:len(elems[i])])

    if xindex == 0:
        return 0

    return (float(equ[equ.index('=')+1: len(equ)+1])+(-numindex)) / xindex
print(equation(input()))

