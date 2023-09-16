# 입력
a, b, c = map(int, input().split())

# 현재로 돌아올 수 있는 경우
# 동일한 숫자가 2개 있을 경우
if a == b or b == c or a == c:
    print("S")

# 두 수의 합이 하나의 수와 같은 경우
elif a+b == c or a+c == b or b+c == a:
    print("S")

# 그 외에는 못 돌아옴
else:
    print("N")