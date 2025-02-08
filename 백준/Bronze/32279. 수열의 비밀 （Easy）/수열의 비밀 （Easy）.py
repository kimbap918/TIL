n = int(input())
p, q, r, s = map(int, input().split())
a = int(input())

sequence = [0] * (n + 1)

for i in range(1, n + 1):
    
    if i == 1:
        sequence[i] = a
        continue

    if i % 2 == 0:
        sequence[i] = (p * sequence[(i // 2)]) + q
    else:
        sequence[i] = (r * sequence[(i // 2)]) + s

print(sum(sequence))