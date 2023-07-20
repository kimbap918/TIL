limit = int(input())
speed = int(input())
d = speed - limit
if d <= 0:
    print("Congratulations, you are within the speed limit!")
elif d >= 1 and d <= 20:
    print("You are speeding and your fine is ${}.".format(100))
elif d >= 21 and d <= 30:
    print("You are speeding and your fine is ${}.".format(270))
elif d >= 31:
    print("You are speeding and your fine is ${}.".format(500))