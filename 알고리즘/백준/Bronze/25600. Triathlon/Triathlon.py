max_value = 0

for _ in range(int(input())) :
    a, d, g = map(int, input().split())
    if a == d + g :
        value = a * (d + g) * 2
    else :
        value = a * (d + g)
    max_value = max(value, max_value)

print(max_value)