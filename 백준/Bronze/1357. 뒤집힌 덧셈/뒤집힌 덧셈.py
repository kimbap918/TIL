A, B = map(list, input().split())

def Rev(x):
    rev = ''
    for i in range(len(x)-1, -1, -1):
        rev += x[i]   
    return rev

rev_a = Rev(A)
rev_b = Rev(B)
rev_c = int(rev_a) + int(rev_b)
Rev(str(rev_c))
result = int(Rev(str(rev_c)))
print(result)