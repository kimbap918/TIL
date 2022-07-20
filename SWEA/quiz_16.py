S = input()
A = list(S)
print(A)

for i in range(len(A)):
    if ord(A[i]) > 96:
        B = ord(A[i]) - 32
        print(chr(B), end = '')
    else:
        print(A[i], end = '')


# 이걸 의도하진 않았겠지
# S = input().upper()
# print(S)
