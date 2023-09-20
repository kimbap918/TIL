direction = ["N", "E", "S", "W"]
result = "N"

for i in range(10):
    command = int(input())
    if command == 1:
        result = direction[(direction.index(result) + 1) % 4]
    elif command == 2:
        result = direction[(direction.index(result) + 2) % 4]
    elif command == 3:
        result = direction[(direction.index(result) + 3) % 4]

print(result)