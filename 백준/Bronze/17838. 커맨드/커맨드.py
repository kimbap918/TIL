for _ in range(int(input())):
    s = input()
    if len(s) == 7 and s[0] != s[2] and s[0] == s[1] == s[4] and s[2] == s[3] == s[5] == s[6]:
        print(1)
    else: print(0)

