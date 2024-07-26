import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    good = 0
    bad = 0
    heros = input().rstrip()
    for word in heros.upper():
        if "B" == word:
            bad += 1
        elif "G" == word:
            good += 1
            
    if good > bad:
        print(f'{heros} is GOOD')
    elif good < bad:
        print(f'{heros} is A BADDY')
    else:
        print(f'{heros} is NEUTRAL')

        
