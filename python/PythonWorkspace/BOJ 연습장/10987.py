mo = ['a', 'e', 'i', 'o', 'u']

word = input()
cnt = 0

for w in word:
    if w in mo:
        cnt += 1

print(cnt)