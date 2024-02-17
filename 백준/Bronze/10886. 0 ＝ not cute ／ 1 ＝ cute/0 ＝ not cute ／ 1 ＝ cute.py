V = int(input())
cute = 0

for _ in range(V):
    if int(input()) == 1:
        cute += 1

if cute > V//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")