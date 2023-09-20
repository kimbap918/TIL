# B를 A로 만들어볼것
# 162 -> 2

A, B = map(int, input().split())
cnt = 1

while A != B:
    cnt += 1
    temp = B
    # B의 끝자리가 1이면
    if B % 10 == 1:
        # 몫 저장
        B //= 10
    # B가 짝수면
    elif B % 2 == 0:
        B //= 2
    # 나눠지지 않으면
    if temp == B:
        print(-1)
        break

else:
    print(cnt)
    

