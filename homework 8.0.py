import re
from itertools import permutations


# Narek
# 1
# For my code input will be like this
# input : 'Oscar Wilde', TheImportanceOfBeingEarnest='Oscar Wilde, 1895', AWomanOfNoImportance='Oscar Wilde, 1895',
#   Hamlet='Shakespeare, 1870', ThePictureOfDorianGray='Oscar Wilde, 1890'

def check(name, **nm):
    return_values = {}
    for key, value in nm.items():
        if name in value:
            val = value.split(', ')
            val[1] = int(val[1])
            if val[1] in return_values.keys():
                return_values[val[1]].append(key)
            else:
                return_values[val[1]] = [key]

    for year in sorted(list(return_values.keys())):
        for book in return_values[year]:
            print(' '.join(re.findall('[A-Z][^A-Z]*', book)))


#check('Oscar Wilde', TheImportanceOfBeingEarnest='Oscar Wilde, 1895', AWomanOfNoImportance='Oscar Wilde, 1895',
  # Hamlet='Shakespeare, 1870', ThePictureOfDorianGray='Oscar Wilde, 1890')

# 2
def biggest(arr):
    big = []
    for array in list(permutations(arr, 3)):
        big.append(array[0]*array[1]*array[2])
    return max(big)


#print(biggest([9, 5, 8, 5, 20, 1, 2, -3, -2, -1, 0]))

# Ruben
# 1

def answer_queries(k, *query_counts):
    query_counts = list(query_counts)
    if len(set(query_counts)) == 1 and query_counts[0] == k:
        return len(query_counts)+1
    if len(query_counts) == 1:
        return query_counts[0]//k+1
    for num in range(len(query_counts)):
        if query_counts[num] > k:
            query_counts[num + 1] += query_counts[num] - k
        elif query_counts[num] == k:
            continue
        else:
            return num + 1


print(answer_queries(3,  100))

# 2
def non_decreasing_sequence(*nums):
    nums = list(nums)
    absnum = [abs(num) for num in nums]
    sortnums = sorted(nums)
    if 0 not in nums:
        if nums == sorted(nums, reverse=True):
            return 'Yes', [-num for num in nums]
        if absnum == sorted(absnum):
            return 'Yes', absnum
        else:
            for i in range(len(absnum)-1):
                if absnum[i] < absnum[i + 1]:
                    for j in range(i):
                        if absnum[j] > 0:
                            absnum[j] -= absnum[j]*2
                    if absnum == sorted(absnum):
                        return 'Yes', absnum
                    else:
                        return 'No'
    else:
        if nums[0] == 0:
            if nums == sortnums:
                return 'Yes', nums
            else:
                return 'No'
        else:
            for i in range(nums.index(0)+1):
                if nums[i] > 0:
                    nums[i] -= nums[i]*2
            if sorted(nums) == nums:
                return 'Yes', nums
            else:
                return 'No'



#print(non_decreasing_sequence(7, 5, 4, 3, 2, 1))
