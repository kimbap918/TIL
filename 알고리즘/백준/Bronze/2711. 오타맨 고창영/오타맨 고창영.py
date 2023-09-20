T = int(input())
for i in range(T):
    miss, spell = map(str, input().split())
    spell = list(spell)
    spell.pop(int(miss)-1)

    for j in range(len(spell)):
        print(spell[j], end = '')
    print()