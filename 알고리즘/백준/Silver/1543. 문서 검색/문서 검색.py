doc = input()
search = input()
cnt = 0
n = 0
while n  <= len(doc) - len(search): # 문서 길이에서 검색길이를 뺀 값이 n보다 크거나 같을때까지
    if doc[n:n+len(search)] == search: # doc의 n부터 n+검색길이 값이 검색과 같다면?
        cnt += 1 # 카운트 증가
        n += len(search) # 검색길이만큼 인덱스를 증가 
    else: # 찾을수 없으면
        n += 1 # 인덱스를 1씩 올려주며 탐색
        
print(cnt)
