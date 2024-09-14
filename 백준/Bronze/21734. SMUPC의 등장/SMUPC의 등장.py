alphabets = list(input())
for i in range(len(alphabets)):
    times = sum(list(map(int, list(str(ord(alphabets[i]))))))
    print(alphabets[i] * times)