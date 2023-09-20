table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
res = ''

while N != 0:
    res += str(table[N%B])
    N = N // B

print(res[::-1])