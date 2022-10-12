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
    l_list = []
    for i in range(5):
        lotto = random.sample(range(1, 46),6)
        l_list.append(lotto)    
    context = {
        'lotto' : l_list,
    }
    return render(request, 'lotto.html', context)