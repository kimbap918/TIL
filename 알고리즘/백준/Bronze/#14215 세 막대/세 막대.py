#  각 막대의 길이는 양의 정수이다
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 삼각형의 둘레를 최대로 해야 한다.

# 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 된다는 점을 사용하면 쉽게 풀 수 있다.

bucket = sorted(map(int, input().split()))
res = bucket[0] + bucket[1] + min(bucket[2], bucket[0]+bucket[1]-1)

print(res)