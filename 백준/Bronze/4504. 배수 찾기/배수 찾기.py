n = int(input())
number = int(input())

while number:
    if number % n == 0:
        print("%s is a multiple of %s." % (number, n))
    else:
        print("%s is NOT a multiple of %s." % (number, n))
    number = int(input())