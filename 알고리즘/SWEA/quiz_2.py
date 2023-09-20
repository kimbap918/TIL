# 1545
T = int(input())
a = []
 
for test_case in range(0, T + 1):
    a.append(test_case)
a.reverse()
 
for i in range(len(a)):
    print(a[i], end=' ')

