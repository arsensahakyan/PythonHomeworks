# 1
def fake_coin(list, start, end):
    # print(list[start:end+1])
    # print(sum(list[start:end+1]))
    if sum(list[start:end+1]) == 5 or sum(list[start:end+1]) == 3:
        for i in range(start, end+1):
            if list[i] == 1:
                return i
    else:
        start += 3
        end1 = end + 3 if(start < 6) else(end + 2)
        return fake_coin(list, start, end1)

print(fake_coin([2,2,2,2,2,2,2,1], 0, 2))

# 2
def func(string):
    if '(' not in string:
        return string
    else:
        string = list(string)
        c = string.count('(')
        indexes = [i for i in range(len(string)) if string[i] in '()']
        str1 = ''.join(string[:indexes[c - 1]])+''.join(list(reversed(string[indexes[c - 1] + 1:indexes[c]])))\
               + ''.join(string[indexes[c]+1:])
        return func(str1)


print(func('foo(bar(baz))blim'))
