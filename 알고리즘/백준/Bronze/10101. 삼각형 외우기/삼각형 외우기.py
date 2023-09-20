angle = []
sum = 0
for _ in range(3):
    tri = int(input())
    angle.append(tri)
    sum += tri

if sum == 180:
    if angle[0] == angle[1] == angle[2]:
        print("Equilateral")
    elif angle[0] != angle[1] != angle[2] and angle[0] != angle[2] != angle[1]:
        print("Scalene")
    else:
        print("Isosceles")
else:
    print("Error")
    
