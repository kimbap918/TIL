N, M = map(int, input().split())
if N != 0:
    books = list(input().split())
    box = 1
    weight = 0

    for i in range(len(books)-1):
        if weight < M:
            weight += int(books[i])

            if weight + int(books[i+1]) > M:
                box += 1
                weight = 0

else:
    box = 0

print(box)



# 5 13
# 13 3 5 4 13 