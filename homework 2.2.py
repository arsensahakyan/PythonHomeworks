# 1
 input_values = []
 dict_of_values = {}
 inp = input()
 while inp != "End":
     input_values.append(inp)
     inp = input()

 for elem in input_values:
     if not dict_of_values.get(elem, False):
         dict_of_values[elem] = 1
     else:
         dict_of_values[elem] += 1

# 2
def check_padindrome(string):
    list_of_chars = []
    for i in range(len(string)):
        if string[i] in list_of_chars:
            list_of_chars.remove(string[i])
        else:
            list_of_chars.append(string[i])
    if len(string) % 2 == 0 and len(list_of_chars) == 0 or (len(string) % 2 == 1 and len(list_of_chars) == 1):
        return True
    else:
        return False
print(check_padindrome(input()))
