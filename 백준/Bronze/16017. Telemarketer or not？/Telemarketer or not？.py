li = [int(input()) for _ in range(4)]
if li[0] in [8,9] and li[-1] in [8, 9] and li[1] == li[2]:
    print("ignore")
else:
    print("answer")