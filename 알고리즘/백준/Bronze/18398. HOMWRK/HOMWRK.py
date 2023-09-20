test_case = int(input())
for i in range(test_case):
    problems = int(input())
    for j in range(problems):
        numbers = list(map(int, input().split()))
        print(numbers[0]+numbers[1], numbers[0]*numbers[1])
 
