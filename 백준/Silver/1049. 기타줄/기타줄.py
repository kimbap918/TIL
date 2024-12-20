N, M = map(int, input().split())
arr_1, arr_2 = [], []
res = 0
# 기타줄의 개수 N
# 기타줄 브랜드(종류) M


# 기타줄 6개 패키지 가격
# 낱개로 살때의 가격

for i in range(M):
    strings, string = map(int, input().split())
    arr_1.append(strings)
    arr_2.append(string)


cheap_strs = min(arr_1)
cheap_str = min(arr_2)


case_1 = N * cheap_str
case_2 = (N // 6+1) * cheap_strs
case_3 = (N // 6) * cheap_strs + (N % 6) * cheap_str

print(min(case_1, case_2, case_3))