from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    return render(request, 'authapp/index.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authapp:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'authapp/signup.html', context)

def accounts(request):
    accounts = get_user_model().objects.order_by('-pk')
    context = {
        'accounts': accounts
    }
    return render(request, 'authapp/accounts.html', context)


def detail(request, pk):
  # 유저를 참조할땐 상속을 받고있기때문에 get_user_model을 import 해서 함수로 참조
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user
    }
  return render(request, 'authapp/detail.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('authapp:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
  auth_logout(request)
  return redirect('authapp:index')