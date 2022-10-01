from django.urls import path
from . import views

"""
메인(R) : 게시글의 목록(/posts) / 게시글 상세
작성(C) : 글을 작성하는 페이지 / 작성 완료
수정(U) : 글을 수정하는 페이지 / 수정 완로
삭제(D) : 글 삭제 완료

"""

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk_>', views.detail, name='detail'),
    path('edit/<int:pk_>', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),

]