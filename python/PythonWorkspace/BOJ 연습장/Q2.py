S = input() # 02984
result = int(S[0]) # 0

for i in range(1, len(S)): # 1~4
    num = int(S[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
