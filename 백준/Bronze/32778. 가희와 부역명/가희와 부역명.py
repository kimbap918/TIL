name = input()

if "(" in name:
    start, end = name.index("("), name.index(")")
    print(name[: start - 1])
    print(name[start + 1 : end])
else: 
    print(name + "\n-")
