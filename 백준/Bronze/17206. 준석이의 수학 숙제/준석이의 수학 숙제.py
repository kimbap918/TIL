T = int(input())
N = list(map(int, input().split()))

lst = [0] * 80001
ans = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        ans += i
    lst[i] = ans


for j in N:
    print(lst[j])
