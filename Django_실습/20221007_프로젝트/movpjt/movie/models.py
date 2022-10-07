from django.db import models


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30) # 리뷰 제목
    content = models.TextField(null=False) # 리뷰 내용
    movie_name = models.CharField(max_length=30) # 영화 이름
    grade = models.DecimalField(max_digits=2, decimal_places=1) # 영화 평점
    created_at = models.DateTimeField(auto_now_add=True) # 리뷰 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 리뷰 수정시간


