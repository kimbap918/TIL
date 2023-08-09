N, A, B = map(int, input().split())

if A < B:
    print("Bus")
elif A > B:
    print("Subway")
else:
    print("Anything")