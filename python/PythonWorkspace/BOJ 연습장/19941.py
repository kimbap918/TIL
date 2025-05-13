# 20 1
# HHPHPPHHPPHPPPHPHPHP

N, K = map(int, input().split())
ham = list(input())
cnt = 0

def find(back, forward):
    global cnt
    for i in range(back, forward):
        if 0 <= i < N and ham[i] == "H":
            ham[i] = "E"
            cnt += 1
            break

for i in range(N):
    if ham[i] == "P":
        find(i-K, i+K+1)

print(cnt)