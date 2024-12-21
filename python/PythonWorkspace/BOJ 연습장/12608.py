cal = {1:['1'], 2:['a', 'b', 'c']}
t = input()


for i, j in cal.items():
    if t in j:
        print(i)
