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
# django.urls 안에 include 작성
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # 서브 URL들에 대한 설정을 '포함' 하게 만드는것
    path('articles/', include('articles.urls')),
    path('practices/', include('practices.urls')),
    path('posts/', include('posts.urls')),
]
