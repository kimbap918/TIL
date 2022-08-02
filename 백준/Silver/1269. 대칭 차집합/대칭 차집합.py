A, B = map(int, input().split())
a = set(list(input().split()))
b = set(list(input().split()))

print(len(a - b) + len(b - a))