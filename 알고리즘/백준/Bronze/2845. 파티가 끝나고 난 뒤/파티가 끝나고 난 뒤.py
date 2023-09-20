a, b = map(int, input().split())
people = list(map(int, input().split()))
party = a * b
for i in people:
    print(i - party, end=' ')