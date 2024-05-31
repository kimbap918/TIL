a = input()
word = 'ILOVEYONSEI'
result = 0

for i in range(len(word)) :
    result += abs(ord(word[i]) - ord(a))
    a = word[i]

print(result)
