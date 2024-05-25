N = int(input())
gifticon = 0
for _ in range(N) :
    period = input()
    if int(period[2:]) <= 90 :
        gifticon += 1
print(gifticon)