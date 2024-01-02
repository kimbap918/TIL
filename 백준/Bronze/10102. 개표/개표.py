v = int(input())
s = input()
a = s.count('A')
if 2*a == v:
    print("Tie")
elif 2*a > v:
    print('A')
else:
    print('B')