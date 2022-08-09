import sys
eng = 'abcdefghijklmnopqrstuvwxyz'
result = []
inp = sys.stdin.read()

for i in eng:
    result.append(inp.count(i))

m = max(result)
for i in range(len(result)):
    if m == result[i]:
        print(chr(i+97), end = '')