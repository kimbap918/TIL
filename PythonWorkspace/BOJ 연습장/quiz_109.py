A, B = input().split()

max_v = int(A.replace('5', '6')) + int(B.replace('5', '6'))
min_v = int(A.replace('6', '5')) + int(B.replace('6', '5'))

print(min_v, max_v)




