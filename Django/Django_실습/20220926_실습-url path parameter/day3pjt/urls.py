"""day3pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from practices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index.urls),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('is-odd-even/<int:_number>', views.is_odd_even),
    path('calculate/<int:_number1>/<int:_number2>', views.calculate),
    path('random_life/', views.random_life),
    path('priv_life/', views.priv_life),
    path('rorem/', views.rorem),
    path('ipsum/', views.ipsum),

]
