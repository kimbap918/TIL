from django.shortcuts import render
import random

# Create your views here.
def lunch(request):

    menus = ['삼겹살', '라면', '돈까스', '초밥']
    menu_num = menus.index(random.choice(menus))
    menu = menus[menu_num]
    images = [ 
            'https://cdn.mindgil.com/news/photo/202103/70839_7148_1250.jpg',
            'https://health.chosun.com/site/data/img_dir/2020/09/07/2020090702900_0.jpg',
            'https://w.namu.la/s/05876ba153ccefcc901768e02f6d6da1e40920e5f9264e11e72f1c0ba7af0ae23ea0f7d2676ee5680d1ac133716d091a45d07919e9f523d1d619732f7b83974262ef9d4e73a2220e77166dfa460434571062091f448f259599aabe2ed23cb57fd68b58e0b6eb5d30c4a9ee88d856c685',
            'https://hajl.athuman.com/karuta/uploads/6e45128aad8bdcf39055b81840ecbe0186605633.jpeg', 
            ]
    image = images[menu_num]
    context = {
        'menu' : menu,        
        'lunch' : image,
        }
    return render(request, 'lunch.html', context)

def lotto(request):
    # 로또 번호 6개를 5번 뽑기
    lotto_list = []
    for _ in range(5):
        lotto = random.sample(range(1,46),6)
        lotto_list.append(lotto)

    lotto_result_list = [
        {"lotto": [1,2,3,4,5,6], "result":"1등 - 10억"},
        {"lotto": [1,2,3,4,5,6], "result":"1등 - 10억"},
        {"lotto": [1,2,3,4,5,6], "result":"1등 - 10억"},
        {"lotto": [1,2,3,4,5,6], "result":"1등 - 10억"},
        {"lotto": [1,2,3,4,5,6], "result":"1등 - 10억"},
    ]
    context = {
        "lotto_list": lotto_list,
    }

    return render(request, 'lotto.html', context)

def today_beer(request):
    beer_list = [
        {"name": "에델바이스", "src": "https://ppss.kr/wp-content/uploads/2021/07/1-10.jpg"},
        {"name": "테라", "src": "https://file.mk.co.kr/meet/neds/2020/12/image_readtop_2020_1267608_16075405834464680.jpg"},
    ]
