from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'practices/index.html')

def ping(request):
    return render(request, 'practices/ping.html')

def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.Get.get('ball'))
    return render(request, 'practices/pong.html', {'name': request.GET.get('ball')})

def is_odd_even(request, _number):
    if _number % 2 == 0:
        ans = "짝수"
    elif _number % 2 == 1:
        ans = "홀수"
    else:
        ans = "0"
    context = {
                "number": _number,
                "ans": ans,
                }
    return render(request, "practices/is_odd_even.html", context)

def calculate(request, _number1, _number2):
    ans_plus = _number1 + _number2
    ans_minus = _number1 - _number2
    ans_multiple = _number1 * _number2
    ans_divide = _number1 // _number2

    context = {
        "number1" : _number1,
        "number2" : _number2,
        "plus" : ans_plus,
        "minus" : ans_minus,
        "multiple" : ans_multiple,
        "divide" : ans_divide,
    }
    return render(request, "practices/calculate.html", context)

def random_life(request):
    return render(request, "practices/random_life.html")

def priv_life(request): 
    life_list = ['말', '소', '돼지', '닭', '쥐', '개', '용', '원숭이', '사람', '토끼', '뱀', '스파게티 코드']
    ans = random.choice(life_list)

    return render(request, 'practices/priv_life.html', {'name': request.GET.get('ball'), 'ans' : ans})

def rorem(request):
    return render(request, 'practices/rorem.html')

def ipsum(request):
    moondan = request.GET.get('ball1')
    daneo = request.GET.get('ball2')
    dan_list = ['김치', '치즈', '김밥']
    dan = random.sample(dan_list, k=1)
    res = dan[0]
    context = {
        'md' : int(moondan),
        'de' : int(daneo),
        'dan' : res,
    }
    return render(request, 'practices/ipsum.html', context)