# 입력
A, B, C = map(int, input().split())

# 출력
res = max([A, B, C])*3 - sum([A, B, C])
print(res)