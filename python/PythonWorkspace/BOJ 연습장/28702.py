# i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.
# i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.
# i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.
# i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.

def fizbuz(i):
    res = ""
    if i % 3 == 0 and i % 5 == 0:
        res = "FizzBuzz"
    elif i % 3 == 0 and i % 5 != 0:
        res = "Fizz"
    elif i % 3 != 0 and i % 5 == 0:
        res = "Buzz"
    else:
        res = i
    return res

arr = ['11', 'Fizz', '13']


for i in range(3):
    print(isinstance(arr[i], int))