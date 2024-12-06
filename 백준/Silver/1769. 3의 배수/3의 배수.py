X = input().strip()  # 입력 값
cnt = 0  # 변환 횟수

# X를 계속 변환하여 한 자리 숫자가 될 때까지 반복
while len(X) > 1:
    X = str(sum(map(int, X)))  # 각 자리 숫자의 합을 계산
    cnt += 1

# 최종 변환 횟수 출력
print(cnt)

# 한 자리 숫자가 3의 배수인지 확인
if int(X) % 3 == 0:
    print("YES")
else:
    print("NO")
