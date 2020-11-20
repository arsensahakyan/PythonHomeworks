# Narek

# 1
def print_num(num):
    lst = [i for i in range(1, num+1)]
    i = 1
    j = 0
    next_ = 2
    while lst[j:i]:
        print(*tuple(lst[j: i]))
        j = i
        i += next_
        next_ += 1


# 2
def successful_number(list_):
    k = len(list_) // 2
    i = k
    while i != 0 and i != len(list_)-1:
        if list_[i] == i:
            return i
        elif list_[i] > k:
            i -= 1
        else:
            i += 1
    return -1


print(successful_number([-1, 0, 6]))
