# 입력
a, p = map(int, input().split())

# 출력
if a*7 > p*13:
    print("Axel")
elif a*7 < p*13:
    print("Petra")
else:
    print("lika")