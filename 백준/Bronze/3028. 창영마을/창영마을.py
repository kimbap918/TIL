li = [1, 0, 0]
s = input()
for c in s:
    if c == 'A':
        li[0], li[1] = li[1], li[0]
    elif c == 'B':
        li[1], li[2] = li[2], li[1]
    else:
        li[0], li[2] = li[2], li[0]
print(li.index(1) + 1)