s = input()
li = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for c in s:
    li.remove(c)
res = ''.join(li)
print(res)