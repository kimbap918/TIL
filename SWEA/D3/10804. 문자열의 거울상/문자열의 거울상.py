T = int(input())

for i in range(1, T+1):
    S = input()

    mirror = ''
    for j in range(len(S)-1, -1, -1):
        if S[j] == "b":
            mirror += "d"
        elif S[j] == "d":
            mirror += "b"
        elif S[j] == "p":
            mirror += "q"
        else:
            mirror += "p"
    print("#{} {}".format(i, mirror))
