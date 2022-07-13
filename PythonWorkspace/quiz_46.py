s = input().lower # 입력받은 문자를 전부 소문자로 바꿈 mississipi 
A = list(set(s)) # 입력받은 문자의 중복을 제거  ['m', 'i', 's', 'p']

print(A)                



# B = []
# C = []
# cnt = 0
# for j in range(65, 91):
#     B.append(chr(j)) # chr() 아스키 코드를 문자로

# for k in range(97, 123):
#     C.append(chr(k))

# for h in range(len(C)): # 소문자의 리스트
#     for i in range(len(A)): # 입력한 값의 리스트
#        if A[i] == C[h]:
#         cnt = A.count(i)
#     print(cnt)
        
