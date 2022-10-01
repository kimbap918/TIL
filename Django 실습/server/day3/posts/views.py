from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
# 첫번째 read
# 데이터의 목록을 출력
def index(request):
    # 모든 글 목록을 보여준다
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.object.all()

    # 2. template에 보내준다.
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)
    

def new(request):
    return render(request, 'posts/new.html')

def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    post = Post.objects.get(pk = pk_)
    context = {
        "post": post,
    }
    return render(request, 'posts/edit.html', context)

def create(request):
    # DB에 저장
    # parameter로 날아온 데이터를 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')

    Post.objects.create(title=title, content=content)
    
    context = {
        'title': title,
        'content': content,
    }

    return redirect('posts:index')
    # return render(request, 'posts/create.html', context)

def update(request, pk_):
    # update할 특정 데이터를 불러온다 -> pk_를 사용
    post = Post.objects.get(pk = pk_)
    title_ = request.GET.get('title')
    content_ = request.GET.get('content')

    # 불러온 제목과 내용의 값을 내가 수정한 값으로 변경
    post.title = title_
    post.content = content_

    # 데이터를 수정한 것을 반영
    post.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect('posts:detail', post.pk)

def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete

    return redirect('posts:index')

# 두번째 read
# 하나의 데이터에 대한 정보를 출력
def detail(request, pk_):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다.
    # 불러온 데이터를 변수에 할당
    post = Post.objects.get(pk = pk_)

    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)