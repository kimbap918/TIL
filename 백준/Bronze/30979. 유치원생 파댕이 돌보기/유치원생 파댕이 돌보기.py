T = int(input())
N = int(input())
F = list(map(int, input().split()))

if T <= sum(F):
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
