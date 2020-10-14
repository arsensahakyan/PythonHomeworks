# 1
output = []
for a in range(0, 101):
    for b in range(0, 101):
        c = a**b
        if c == b**a and c <= 100:
            if [b, a, c] in output:
                continue
            output.append([a, b, c])
print(output)

# 2
for i in range(1, 5):
    for j in range(1, i+1):
        print(i, end="")
    print()