from collections import Counter
while True:
    S = Counter(input())
    if S['*'] == 1:
        break
    if S[' '] >= 1:
        del S[' ']
    if len(S) >= 26:
        print("Y")
    else:
        print("N")