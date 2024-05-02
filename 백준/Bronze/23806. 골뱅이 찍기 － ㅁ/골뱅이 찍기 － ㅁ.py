N = int(input())

for _ in range(N):
    print('@'*(5*N))

for _ in range(N*3):
    print('@'*N + ' '*(N*3) + '@'*N)

for _ in range(N):
    print('@'*(5*N))