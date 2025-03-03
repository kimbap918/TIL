import sys

def string_to_binary(string):
    
    return bin(int(string))[2:].rjust(6, '0')

N = int(sys.stdin.readline())

for _ in range(N):
    H, M, S = map(string_to_binary, sys.stdin.readline().split(':'))

    col = ''.join([h + m + s for h, m, s in zip(H, M, S)])
    row = H + M + S

    print(f'{col} {row}')