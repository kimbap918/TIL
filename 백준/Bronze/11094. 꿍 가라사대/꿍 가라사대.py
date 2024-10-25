N = int(input())

for _ in range(N):
    command = input()
    if command[:10] == "Simon says":
        print(command[10:])
