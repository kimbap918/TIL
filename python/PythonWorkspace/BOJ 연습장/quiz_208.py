words = input()
rev_words = []
for word in reversed(words):
    rev_words.append(word)
print(''.join(rev_words))
