# Narek

# 1
def print_num(num):
    lst = [i for i in range(1, num+1)]
    return_vals = []
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
    n = [i for i in range(len(list_))]
    k = list(filter(lambda x: x == list_[x], n))
    return k[0] if k else -1
