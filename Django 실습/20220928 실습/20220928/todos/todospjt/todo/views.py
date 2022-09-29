# redirect 사용을 위해 import
from django.shortcuts import render, redirect
# db에 저장하기 위해 model을 import
from .models import Todo

# Create your views here.
def index(request):
    # models에서 정의한 Todo의 모든 정보를 가져와서 _todos에 저장 
    _todos = Todo.objects.all()
    # _todos의 정보를 context에 담아서 반환하게함
    context = {
        "todos" : _todos,
    }
    return render(request, 'todo/index.html', context)

def create(request):
    # input에서 입력받은 값을 content에 저장 
    content = request.GET.get("content_")
    priority = request.GET.get("priority_")
    deadline = request.GET.get("deadline_")
    # db에 저장, create(필드, 값) 
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    _todos = Todo.objects.all()
    context = {
        "todos" : _todos,
    }

    return redirect('todo:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()

    return redirect('todo:index')

def update(request, pk):
    # update할 특정 데이터를 불러온다 -> pk_를 사용
    todo = Todo.objects.get(pk = pk)
    completed_ = True

    # 불러온 제목과 내용의 값을 내가 수정한 값으로 변경
    todo.completed = completed_

    # 데이터를 수정한 것을 반영
    todo.save()

    return redirect('todo:index')