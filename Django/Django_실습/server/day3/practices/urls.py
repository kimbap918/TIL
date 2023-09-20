from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('is-odd-even/<int:_number>', views.is_odd_even),
    path('calculate/<int:_number1>/<int:_number2>', views.calculate),
    path('random_life/', views.random_life),
    path('priv_life/', views.priv_life),
    path('rorem/', views.rorem),
    path('ipsum/', views.ipsum),
]