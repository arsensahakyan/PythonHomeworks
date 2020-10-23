# Ruben
# 1
# 2
# def problemTwo(string):
#     vowel = []
#     consonant = []
#     for i in range(1, len(string)+1):
#         start = 0
#         end = start + i
#         while end <= len(string):
#             if string[start:end][0] in 'aeiou':
#                 vowel.append(string[start:end])
#             else:
#                 consonant.append(string[start:end])
#             start += 1
#             end = start + i
#     v = {}
#     c = {}
#     for elem in set(vowel):
#         v[elem] = vowel.count(elem)
#     for elem in set(consonant):
#         c[elem] = consonant.count(elem)
#
#     return v, c
#
# print(problemTwo(input()))

