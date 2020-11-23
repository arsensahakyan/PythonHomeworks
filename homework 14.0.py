# Narek
# 1
def same_or_not(str1, str2):
    return sorted(str1) == sorted(str2)


# 2
def search(lst, num):
    for i in range(len(lst)):
        if lst[i][0] <= num <= lst[i][-1]:
            l = 0
            r = len(lst) - 1
            mid = len(lst[i]) // 2
            while l <= r:
                if num > lst[i][mid]:
                    r = mid
                    mid += len(lst[r:])//2
                elif num < lst[i][mid]:
                    l = mid
                    mid -= len(lst[:l + 1])//2
                else:
                    return i, mid
    return -1


print(search([[10, 20, 30, 40],
 [15, 25, 35, 45],
 [27, 29, 37, 48],
 [32, 33, 39, 50]], 29))