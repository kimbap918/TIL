from itertools import combinations
num = list(map(int, input().split()))
twos = [i|j for i, j in combinations(num, 2)]
triples = [i|j|k for i, j, k in combinations(num, 3)]
total = 0
for i in twos:
    total ^= i
for j in triples:
    total ^= j
print(total)
