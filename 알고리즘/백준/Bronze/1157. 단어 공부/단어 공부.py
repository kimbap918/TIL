s = input().lower() # 입력받은 문자를 전부 소문자로 바꿈 mississipi 
A = list(set(s)) # ['m', 'i', 's', 'p']
cnt = [] # 많이 사용된 문자 카운트를 담을 리스트
max = 0

for i in A: # m, i, s, p 에서
  count = s.count(i) # mississipi를 비교하여 사용된 단어 카운트
  cnt.append(count) # 카운트값을 리스트에 추가 

for j in range(len(cnt)): # 최대로 많이 사용된 값 구하기
  if max < cnt[j]:
    max = cnt[j]

if cnt.count(max) >= 2: # 최대값의 카운트가 2가지거나 그 이상일경우
  print("?") # ? 출력
else:
  print(A[cnt.index(max)].upper())
  # 카운트에서 최대값의 인덱스를 가져와 A[]에서 찾아내고 대문자로 출력 
