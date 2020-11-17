# Narek
# 1
def find_length_of_number(num):
    ind = [10, 1]

    while True:
        if num//ind[0] == 0:
            break
        else:
            ind[0] *= 10
            ind[1] += 1
    return ind[1]


print(find_length_of_number(352))


# 2
def func(lst, num):
    ret_vals = set()
    for i in range(len(lst)):
        test = lst.copy()
        test.remove(lst[i])
        if num - lst[i] in test:
            ret_vals.add((lst[i], num-lst[i]))
            ret_vals.add((num - lst[i], lst[i]))
        test = lst.copy()
    return ret_vals


print(*func([5, 2, 2, 5, 3, 4, 4],8))
