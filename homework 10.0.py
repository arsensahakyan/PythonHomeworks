# Narek
# 1
def biggest_abs_sum(lst):
    biggest_sum = 0
    for num in range(0, len(lst), 2):
        if abs(lst[num] - lst[num + 1]) > biggest_sum:
            biggest_sum = abs(lst[num] - lst[num + 1])
    return biggest_sum

print(biggest_abs_sum([5,9,2,12,5,8]))

# 2
def count_of_twos(n):
    k = 0
    for j in range(n):
        if '2' in str(j):
            k += str(j).count('2')
    return k
