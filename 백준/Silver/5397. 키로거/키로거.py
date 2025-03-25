import sys
input = sys.stdin.readline

def password(words):
    left, right = [], [] # 커서 왼쪽에 있는 문자, 커서 오른쪽에 있는 문자
    # <<BP<A>>Cd-

    for word in words:
        if word == "<":
            if left:
                right.append(left.pop())
        elif word == ">":
            if right:
                left.append(right.pop())
        elif word == "-":
            if left:
                left.pop()
        else:
            left.append(word)
    return ''.join(left) + ''.join(reversed(right))


T = int(input())

for _ in range(T):
    words = input().rstrip()
    print(password(words))