ML, MR, TL, TR = map(lambda x:"SPR".find(x), input().split())

def lose_case(x):
    return (x+2)%3

if ML == MR and lose_case(ML) in [TL,TR]:
    print("TK")
elif TL == TR and lose_case(TL) in [ML,MR]:
    print("MS")
else:
    print("?")