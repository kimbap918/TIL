from django.urls import path
from . import views # .은 현재경로 라는 뜻, 현재경로의 views를 가져온다. 

# url namespace
# url을 이름으로 분류하는 기능

app_name = "todo"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
]