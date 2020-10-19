# Ruben
# 1
students = []
for i in range(int(input())):
    name = input()
    mark = int(input())
    students.append([name, mark])
print(students)
second_min = list(set(sorted([elem[1] for elem in students])))[1]
print(second_min)
print('\n'.join(sorted([elem[0] for elem in students if elem[1] == second_min])))

# 2
superString = input()
subString = input()
n = [superString.find(n) for n in subString]
print(superString[min(n):max(n)+1])

# Narek
# 1
list = [6, 5, 3, 6, 4]
n = 0
for i in range(1, len(list)-1, 1):
    if list[i] != list[i + 1]-1 and list[i - 1] >= list[i]:
        k = list[i - 1] - list[i] + 1
        list[i] += k
        n += k
k = list[-2] - list[-1] + 1
list[-1] += k
n += k
k = list[1] - list[0] - 1
list[0] += k
n += k
print(list, n)

# 2
def check(arr):
    count = 0
    for number in set(arr):
        if arr.count(number) == 2:
            count += 1
        elif arr.count(number) > 2:
            return False
    for i in range(len(arr)-1):
        del_num = arr.pop(i)
        if arr == sorted(arr):
            return True
        else:
         arr.insert(i, del_num)
    if count > 1:
        return False
    else:
        return True

print(check(nums))
