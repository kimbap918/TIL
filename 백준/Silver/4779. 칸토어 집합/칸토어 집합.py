import sys
for i in sys.stdin: # ex) 3이면 i = 3
    line = "-"
    for j in range(int(i)):
        # 1회 - -
        # 2회 - -   - -
        # 3회 - -   - -         - -   - -
        line = line+" "*len(line)+line
    print(line)