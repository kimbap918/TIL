from sys import stdin
 
def BMI(kg, m):
    return kg/((0.01*m)**2)
 
for _ in range(int(input())):
    m, kg = map(int, stdin.readline().rstrip().split())
    bmi = BMI(kg, m)
    if m < 140.1: print(6)
    elif m < 146: print(5)
    elif m < 159: print(4)
    elif m < 161:
        if bmi < 16 or bmi >= 35: print(4)
        else: print(3)
    elif m < 204:
        if bmi < 16 or bmi >= 35: print(4)
        elif bmi < 18.5 or bmi >= 30: print(3)
        elif bmi < 20 or bmi >= 25: print(2)
        else: print(1)
    else: print(4)