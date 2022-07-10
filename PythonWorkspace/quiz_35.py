A = []
cnt = 0

for i in range(10):
    N = int(input())
    A.append(N%42)

A = len(set(A))
print(A)


# set함수는 리스트에서 중복된값을 없애주는 함수이고, len함수는 리스트의 길이를 구하는 함수다.