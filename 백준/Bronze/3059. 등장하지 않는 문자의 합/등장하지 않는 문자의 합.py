import sys
input = sys.stdin.readline

words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
T = int(input())

for _ in range(T):
    ans = 2015
    S = set(input())
    for word in S:
        if word in words:
            ans -= ord(word)
    print(ans)

