
k = int(input())


fees = 25 + k*0.01

if fees < 100:
    print(100)
elif fees > 2000:
    print(2000)
else:
    print(fees)