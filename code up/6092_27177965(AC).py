n = int(input()) # 출석을 부를 횟수
a = input().split()
d = []
for i in range(0, 24): # d 값(0) 저장
    d.append(0)

for i in range(n): # 출석 번호를 부를 횟수
    a[i] = int(a[i]) # 횟수 저장
  
for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')
