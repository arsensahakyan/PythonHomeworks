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
list = [1, 5, 1]
n = 0
for i in range(1,len(list)):
    numb = list[i-1]-list[i]+1
    if list[i] <= list[i-1]:
        if numb < list[i-1]:
            list[i-1] += list[i-1]+numb
            n += numb
        else:
            list[i] = list[i]+numb
            n += numb
    else:
        if list[i]-list[i-1] != 1:
            numb = list[i]-list[i-1]
            list[i-1] += numb-1
            n += numb-1
print(n)

# 2
nums = [1, 3, 4, 2, 6, 0]
n = 0
for i in range(len(nums)-1):
    if nums[i] >= nums[i+1]:
        n+=1
        if n > 1:
            break
print(n<=1)