import sys
word = input()
words = []

# length = 6
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        part_1 = ''.join(reversed(word[:i]))
        part_2 = ''.join(reversed(word[i:j]))
        part_3 = ''.join(reversed(word[j:]))

        words.append(part_1 + part_2 + part_3)


print(sorted(words)[0])