lst = []
for _ in range(6):
    s = input()
    if s[-1] == " " : lst.append(len(s) - 1)
    else : lst.append(len(s))
print(f"Latitude {lst[0]}:{lst[1]}:{lst[2]}")
print(f"Longitude {lst[3]}:{lst[4]}:{lst[5]}")
