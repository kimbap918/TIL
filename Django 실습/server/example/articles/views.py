from django.shortcuts import render
import random

# Create your views here.
def index(request):
  # 환영하는 메인 페이지를 보여준다.

  names = ['최준혁', '홍길동', '장길산', '김영철', '나진수']
  name = random.choice(names)
  
  context = {
    'name' : name,
    'img' : 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
  
  return render(request, 'index.html', context) # 끝은 항상 render()를 리턴

def welcome(request, name):
  #  사람들이 /welcome/본인이름을 입력하면, 환영 인사와 이름을 동시에 보여준다/

  context = {
    'name' : name,
    }
  return render(request, 'welcome.html', context)
