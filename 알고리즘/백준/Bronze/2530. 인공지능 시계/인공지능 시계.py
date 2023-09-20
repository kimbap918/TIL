H, M, S = map(int, input().split())
D = int(input()) 

S += D % 60
D = D // 60
if S >= 60:
    S -= 60
    M += 1

M += D % 60
D = D // 60
if M >= 60:
    M -= 60
    H += 1

H += D % 24
if H >= 24:
    H -= 24

print(H,M,S)