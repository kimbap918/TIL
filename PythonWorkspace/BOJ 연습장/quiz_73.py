censored = ['C','A','M','B','R','I','D','G','E']
S = input()

for i in censored:
    if i in S:
       S = S.replace(i, "")
print(S)
