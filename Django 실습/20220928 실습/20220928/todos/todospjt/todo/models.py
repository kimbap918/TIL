from django.db import models

# Create your models here.
class Todo(models.Model):
    # django에서 pk는 자동으로 만들어준다.
    content = models.CharField(max_length = 80)     # 할 일 내용 
    completed = models.BooleanField(default=False)  # 완료 여부
    priority = models.IntegerField(default=3)       # 우선순위
    created_at = models.DateField(auto_now_add=True)# 생성 날짜
    """
    default 
    데이터를 생성할 때 값을 안넣으면 
    자동으로 값을 채워서 데이터를 생성하겠다.
    """
    deadline = models.DateField(null=True)          # 마감 기한

