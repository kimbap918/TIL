li = []
for i in range(31):
    li.append(2**i)
if int(input()) in li:
    print(1)
else:
    print(0)