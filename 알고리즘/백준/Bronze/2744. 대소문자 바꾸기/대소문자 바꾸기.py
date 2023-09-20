words = input()
ans = []
for word in words:
    if ord(word) >= 97 and ord(word) <= 122:
        ans.append(word.upper())
    else:
        ans.append(word.lower())
print(''.join(ans))