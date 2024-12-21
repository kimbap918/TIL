# X = input()
# cnt = 0

# while True:
#     if int(X) < 10 and int(X) % 3 != 0:
#         print("NO")
#         break
#     elif int(X) % 3 == 0:
#         print("YES")
#         break


#     cnt += 1
#     num = 0
#     for i in X:
#         num += int(i)

#     if (num % 3) != 0:
#         X = str(num)
#         continue


# print(cnt)


# 1+2+3+4+5+6+7 = 28
# 28 % 3 = 1

# 2+8 = 10
# 10 % 3 = 1

# 1+0 = 1
# 1 % 3 = 1


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
