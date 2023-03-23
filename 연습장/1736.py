A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())
temp = 0

def GCD(A, B):
    while B != 0:
        tmp = A % B
        A = B
        B = tmp
    return A


temp_B1 = B1
temp_B2 = B2

B1 = B1 * B2
B2 = temp_B1 * B2

A1 = temp_B2 * A1
A2 = temp_B1 * A2

md= GCD(A1+A2, B1)

if (A1+A2) % md == 0 and B1 % md == 0:
    print(int((A1+A2)/md), int(B1/md))




