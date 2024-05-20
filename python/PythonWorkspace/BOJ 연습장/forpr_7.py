a = "369"
b = "693"

strike = 0
ball = 0

for number in a:
    # 3 6 9

    # 
    if b.count(number) >= 1:        
        if b.find(number) != a.find(number):
            strike += 1
        else:
            ball += 1

print("Strike:", strike, "Ball:", ball)