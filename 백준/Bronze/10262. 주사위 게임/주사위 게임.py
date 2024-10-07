a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())
Ga, Gb = a1+a2, b1+b2
Ea, Eb = a3+a4, b3+b4
if Ga-Ea + Gb-Eb == 0:
    print("Tie")
elif Ga-Ea + Gb-Eb > 0:
    print("Gunnar")
else:
    print("Emma")