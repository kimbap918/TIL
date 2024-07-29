sentence = input()
i = 0
vowels = ['a', 'e', 'i', 'o', 'u']
while i < len(sentence):    # for -> range error
    print(sentence[i], end='')
    if sentence[i] in vowels:
        i += 2
    i += 1