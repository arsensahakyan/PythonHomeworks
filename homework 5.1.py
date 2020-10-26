# Ruben
# 2
# number = 0
# bag = []
#
# def add_item(itemName, itemCost):
#     bag.append(itemName)
#     bag.append(itemCost)
#
# def print_receipt():
#     global number
#     global bag
#     number += 1
#     print(f'Cheque {number}. Count of things : {len(bag)//2}')
#     for elem in range(0, len(bag), 2):
#         print(bag[elem], '-', bag[elem + 1])
#     print(f'Amount : {sum([bag[elem] for elem in range(1, len(bag), 2)])}')
#     print('-----')
#     bag = []

# 1
# def check():
#     clubs = {}
#     clubs_surnames = {}
#     exp = input().replace(' ', '')
#     for elem in exp.split(','):
#         clubs[elem[0:elem.find(':')]] = int(elem[elem.find(':')+1:])
#     for i in range(len(clubs)):
#         inp = input().replace(' ', '').split(',')
#         clubs_surnames[list(clubs.keys())[list(clubs.values()).index(len(inp))]] = inp
#     students = input().replace(' ', '').split(',')
#     minn = [0 for elem in students]
#     for i in range(len(students)):
#         for elem in clubs_surnames:
#             if students[i] in clubs_surnames[elem]:
#                 minn[i] += 1
#     k = [elem for elem in students if minn[students.index(elem)] == min(minn)]
#     k.sort()
#     return k[0]
#
#
# check()

# Narek
# 1
# def tictactoe(list):
#     for i in range(3):
#         if list[0][i] == list[1][i] == list[2][i]:
#            return list[0][i]
#         elif len(set(list[i])) == 1:
#             return list[i][0]
#     if list[0][0] == list[1][1] == list[2][2]:
#         return list[0][0]
#     elif list[0][2] == list[1][1] == list[2][0]:
#         return list[0][2]
#
# list = [['x', 'o', 'o'], ['o', 'x', 'x'], ['o', 'o', 'x']]
# print(tictactoe(list))
