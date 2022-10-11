from django.urls import path 
from . import views

app_name = 'authapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>', views.detail, name='detail'),
]
