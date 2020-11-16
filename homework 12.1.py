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
    ret_vals = []
    for i in range(len(lst)-1):
        if lst[i] + lst[i + 1] == num:
            ret_vals.append((lst[i], lst[i + 1]))
    return ret_vals


print(func([5, 2, 2, 5, 3],8))
