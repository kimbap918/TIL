N = int(input())
s = "%.300f" % 2 ** -N
end = len(s)
for i in range(end-1, 1, -1):
    if s[i] != '0':
        end = i
        break
print(s[:end+1])