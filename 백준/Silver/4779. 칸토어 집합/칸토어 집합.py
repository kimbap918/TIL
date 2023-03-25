import sys
for i in sys.stdin:
    temp = "-"
    for j in range(int(i)):
        temp = temp+" "*len(temp)+temp
    print(temp)