a, b = input().split()
la, lb = len(a), len(b)
if la > lb:
    b = '0'*(la-lb) + b
else:
    a = '0'*(lb-la) + a
res = ""
for i in range(len(a)):
    res += str(int(a[i]) + int(b[i]))
print(res)