N = int(input())
ary = set()
std_ary = []
for _ in range(N):
    S = input()
    ary.add(S) # set에 담아 중복 제거

for i in ary:
    std_ary.append(i) # 중복 제거된 값을 리스트에 담음

std_ary.sort() # 알파벳순에 따라 정렬
std_ary.sort(key = len) # 길이에 따라 정렬 
for i in std_ary:
    print(i)